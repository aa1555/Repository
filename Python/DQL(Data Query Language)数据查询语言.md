## DQL (Data Query Language) 数据查询语言

关于查询语句有很多，这里基础的不再介绍。主要介绍排序查询、聚合函数、模糊查询、分组查询、分页查询、内连接、外连接、子查询。

### 一、基础关键字

**`BETWEEN...AND`（在什么之间）和 `IN`（集合）**

```sql
-- 查询年龄大于等于20 小于等于30
SELECT * FROM student WHERE age >= 20 && age <= 30;
SELECT * FROM student WHERE age >= 20 AND age <= 30;
SELECT * FROM student WHERE age BETWEEN 20 AND 30;

-- 查询年龄22岁，18岁，25岁的信息
SELECT * FROM student WHERE age = 22 OR age = 18 OR age = 25;
SELECT * FROM student WHERE age IN (22, 18, 25);
```

**`IS NOT NULL`（不为 null 值）、`LIKE`（模糊查询）、`DISTINCT`（去除重复值）**

```sql
-- 查询英语成绩不为 null
SELECT * FROM student WHERE english IS NOT NULL;

-- _: 单个任意字符
-- %: 多个任意字符
-- 查询姓马的有哪些？
SELECT * FROM student WHERE NAME LIKE '马%';
-- 查询姓名第二个字是化的人
SELECT * FROM student WHERE NAME LIKE '_化%';
-- 查询姓名是3个字的人
SELECT * FROM student WHERE NAME LIKE '___';
-- 查询姓名中包含德的人
SELECT * FROM student WHERE NAME LIKE '%德%';

-- 关键词 DISTINCT 用于返回唯一不同的值
-- 语法：SELECT DISTINCT 列名称 FROM 表名称
SELECT DISTINCT NAME FROM student;
```

### 二、排序查询 `ORDER BY`

**语法**：`ORDER BY` 子句  
`ORDER BY 排序字段1 排序方式1, 排序字段2 排序方式2...`

**注意**：  
如果有多个排序条件，则当前边的条件值一样时，才会判断第二条件。

```sql
-- 例子
SELECT * FROM person ORDER BY math; -- 默认升序
SELECT * FROM person ORDER BY math DESC; -- 降序
```

---

### 三、聚合函数：将一列数据作为一个整体，进行纵向的计算

> 1. `COUNT`：计算个数  
> 2. `MAX`：计算最大值  
> 3. `MIN`：计算最小值  
> 4. `SUM`：计算和  
> 5. `AVG`：计算平均数  

### 四、分组查询 `GROUP BY`

**语法**：`GROUP BY 分组字段;`

**注意**：分组之后查询的字段：分组字段、聚合函数

```sql
-- 按照性别分组，分别查询男、女同学的平均分
SELECT sex, AVG(math) FROM student GROUP BY sex;

-- 按照性别分组，分别查询男、女同学的平均分、人数
SELECT sex, AVG(math), COUNT(id) FROM student GROUP BY sex;

-- 按照性别分组，分别查询男、女同学的平均分、人数，要求：分数低于70分的人，不参与分组
SELECT sex, AVG(math), COUNT(id) FROM student WHERE math > 70 GROUP BY sex;

-- 按照性别分组，分别查询男、女同学的平均分、人数，要求：分数低于70分的人，不参与分组，分组之后人数要大于2人
SELECT sex, AVG(math), COUNT(id) FROM student WHERE math > 70 GROUP BY sex HAVING COUNT(id) > 2;
SELECT sex, AVG(math), COUNT(id) 人数 FROM student WHERE math > 70 GROUP BY sex HAVING 人数 > 2;
```

---

### 五、分页查询

1. **语法**：`LIMIT 开始的索引, 每页查询的条数;`  
2. **公式**：开始的索引 = （当前的页码 - 1） * 每页显示的条数  
3. `LIMIT` 是一个 MySQL "方言"

```sql
-- 每页显示3条记录
SELECT * FROM student LIMIT 0, 3; -- 第1页
SELECT * FROM student LIMIT 3, 3; -- 第2页
SELECT * FROM student LIMIT 6, 3; -- 第3页
```

---

### 六、内连接查询

> **1. 从哪些表中查询数据**  
> **2. 条件是什么**  
> **3. 查询哪些字段**

#### 1. 隐式内连接：使用 `WHERE` 条件消除无用数据

```sql
-- 查询员工表的名称，性别，部门表的名称
SELECT emp.name, emp.gender, dept.name FROM emp, dept WHERE emp.dept_id = dept.id;

SELECT 
    t1.name, -- 员工表的姓名
    t1.gender, -- 员工表的性别
    t2.name -- 部门表的名称
FROM
    emp t1,
    dept t2
WHERE 
    t1.dept_id = t2.id;
```

#### 2. 显式内连接

```sql
-- 语法：
SELECT 字段列表 FROM 表名1 [INNER] JOIN 表名2 ON 条件
-- 例如：
SELECT * FROM emp INNER JOIN dept ON emp.dept_id = dept.id;
SELECT * FROM emp JOIN dept ON emp.dept_id = dept.id;
```

---

### 七、外连接查询

#### 1. 左外连接 -- 查询的是左表所有数据以及其交集部分

```sql
-- 语法：
SELECT 字段列表 FROM 表1 LEFT [OUTER] JOIN 表2 ON 条件;
-- 例子：
-- 查询所有员工信息，如果员工有部门，则查询部门名称，没有部门，则不显示部门名称
SELECT t1.*, t2.name FROM emp t1 LEFT JOIN dept t2 ON t1.dept_id = t2.id;
```

#### 2. 右外连接 -- 查询的是右表所有数据以及其交集部分

```sql
-- 语法：
SELECT 字段列表 FROM 表1 RIGHT [OUTER] JOIN 表2 ON 条件;
-- 例子：
SELECT * FROM dept t2 RIGHT JOIN emp t1 ON t1.dept_id = t2.id;
```

---

### 八、子查询：查询中嵌套查询

```sql
-- 查询工资最高的员工信息
-- 1. 查询最高的工资是多少 9000
SELECT MAX(salary) FROM emp;

-- 2. 查询员工信息，并且工资等于9000的
SELECT * FROM emp WHERE emp.salary = 9000;

-- 一条 SQL 就完成这个操作，这就是子查询
SELECT * FROM emp WHERE emp.salary = (SELECT MAX(salary) FROM emp);
```

#### 1. 子查询的结果是单行单列的

子查询可以作为条件，使用**运算符去判断**。运算符：`> >= < <= =`

```sql
-- 查询员工工资小于平均工资的人
SELECT * FROM emp WHERE emp.salary < (SELECT AVG(salary) FROM emp);
```

#### 2. 子查询的结果是多行单列的

子查询可以作为条件，使用**运算符 IN** 来判断

```sql
-- 查询'财务部'和'市场部'所有的员工信息
SELECT id FROM dept WHERE NAME = '财务部' OR NAME = '市场部';
SELECT * FROM emp WHERE dept_id = 3 OR dept_id = 2;

-- 子查询
SELECT * FROM emp WHERE dept_id IN (SELECT id FROM dept WHERE NAME = '财务部' OR NAME = '市场部');
```

#### 3. 子查询的结果是多行多列的

子查询可以作为一张**虚拟表**参与查询

```sql
-- 查询员工入职日期是2011-11-11日之后的员工信息和部门信息
-- 子查询
SELECT * FROM dept t1, (SELECT * FROM emp WHERE emp.join_date > '2011-11-11') t2 WHERE t1.id = t2.dept_id;

-- 普通内连接
SELECT * FROM emp t1, dept t2 WHERE t1.dept_id = t2.id AND t1.join_date > '2011-11-11';
```
