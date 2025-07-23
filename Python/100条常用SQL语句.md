### 一、基本查询语句

**查询所有数据**：
```sql
SELECT * FROM 表名;
```

**查询特定列**：
```sql
SELECT 列名1, 列名2 FROM 表名;
```

**条件查询**：
```sql
SELECT * FROM 表名 WHERE 条件;
```

**模糊查询**：
```sql
SELECT * FROM 表名 WHERE 列名 LIKE '模式%';
```

**排序查询**：
```sql
SELECT * FROM 表名 ORDER BY 列名 ASC|DESC;
```

**限制返回行数**：
```sql
SELECT * FROM 表名 LIMIT 10;
```

**去重查询**：
```sql
SELECT DISTINCT 列名 FROM 表名;
```

### 二、聚合与分组

**聚合函数 - 计数**：
```sql
SELECT COUNT(*) FROM 表名;
```

**分组查询**：
```sql
SELECT 列名, COUNT(*) FROM 表名 GROUP BY 列名;
```

**条件分组**：
```sql
SELECT 列名, COUNT(*) FROM 表名 GROUP BY 列名 HAVING COUNT(*) > 1;
```

**计算总和**：
```sql
SELECT SUM(列名) FROM 表名;
```

**计算平均值**：
```sql
SELECT AVG(列名) FROM 表名;
```

**计算最大值**：
```sql
SELECT MAX(列名) FROM 表名;
```

**计算最小值**：
```sql
SELECT MIN(列名) FROM 表名;
```

### 三、数据操作

**插入数据**：
```sql
INSERT INTO 表名 (列名1, 列名2) VALUES (值1, 值2);
```

**批量插入数据**：
```sql
INSERT INTO 表名 (列名1, 列名2) VALUES (值1, 值2), (值3, 值4);
```

**更新数据**：
```sql
UPDATE 表名 SET 列名 = 新值 WHERE 条件;
```

**删除数据**：
```sql
DELETE FROM 表名 WHERE 条件;
```

### 四、表操作

**创建表**：
```sql
CREATE TABLE 表名 (列名1 数据类型, 列名2 数据类型);
```

**删除表**：
```sql
DROP TABLE 表名;
```

**修改表结构**：
```sql
ALTER TABLE 表名 ADD 列名 数据类型;
```

**删除表中的列**：
```sql
ALTER TABLE 表名 DROP COLUMN 列名;
```

**重命名表**：
```sql
ALTER TABLE 旧表名 RENAME TO 新表名;
```

### 五、索引与视图

**创建索引**：
```sql
CREATE INDEX 索引名 ON 表名 (列名);
```

**删除索引**：
```sql
DROP INDEX 索引名;
```

**创建视图**：
```sql
CREATE VIEW 视图名 AS SELECT * FROM 表名;
```

**删除视图**：
```sql
DROP VIEW 视图名;
```

### 六、连接查询

**内连接**：
```sql
SELECT * FROM 表1 INNER JOIN 表2 ON 表1.列名 = 表2.列名;
```

**左连接**：
```sql
SELECT * FROM 表1 LEFT JOIN 表2 ON 表1.列名 = 表2.列名;
```

**右连接**：
```sql
SELECT * FROM 表1 RIGHT JOIN 表2 ON 表1.列名 = 表2.列名;
```

**全连接**：
```sql
SELECT * FROM 表1 FULL OUTER JOIN 表2 ON 表1.列名 = 表2.列名;
```

### 七、子查询与集合

**子查询**：
```sql
SELECT * FROM 表名 WHERE 列名 IN (SELECT 列名 FROM 其他表名);
```

**存在查询**：
```sql
SELECT * FROM 表名 WHERE EXISTS (SELECT 1 FROM 其他表名 WHERE 条件);
```

**联合查询**：
```sql
SELECT 列名 FROM 表1 UNION SELECT 列名 FROM 表2;
```

### 八、日期与时间

**获取当前时间**：
```sql
SELECT NOW();
```

**获取当前日期**：
```sql
SELECT CURDATE();
```

**日期加法**：
```sql
SELECT DATE_ADD(日期, INTERVAL 1 DAY);
```

**日期减法**：
```sql
SELECT DATE_SUB(日期, INTERVAL 1 DAY);
```

**格式化日期**：
```sql
SELECT DATE_FORMAT(日期, '%Y-%m-%d');
```

### 九、字符串处理

**字符串连接**：
```sql
SELECT CONCAT(列名1, 列名2) FROM 表名;
```

**字符串长度**：
```sql
SELECT LENGTH(列名) FROM 表名;
```

**字符串截取**：
```sql
SELECT SUBSTRING(列名, 1, 5) FROM 表名;
```

**查找字符串位置**：
```sql
SELECT LOCATE('子串', 列名) FROM 表名;
```

**大写转换**：
```sql
SELECT UPPER(列名) FROM 表名;
```

**小写转换**：
```sql
SELECT LOWER(列名) FROM 表名;
```

**去除空格**：
```sql
SELECT TRIM(列名) FROM 表名;
```

### 十、其他高级功能

**使用CASE语句**：
```sql
SELECT 列名, CASE WHEN 条件 THEN '值1' ELSE '值2' END FROM 表名;
```

**使用IF语句**：
```sql
SELECT 列名, IF(条件, '值1', '值2') FROM 表名;
```

**使用COALESCE函数**：
```sql
SELECT COALESCE(列名, '默认值') FROM 表名;
```

**使用NULLIF函数**：
```sql
SELECT NULLIF(列名1, 列名2) FROM 表名;
```

**获取唯一值的数量**：
```sql
SELECT COUNT(DISTINCT 列名) FROM 表名;
```

**使用GROUP_CONCAT**：
```sql
SELECT GROUP_CONCAT(列名) FROM 表名 GROUP BY 其他列名;
```

### 十一、事务管理

**事务开始**：
```sql
BEGIN;
```

**提交事务**：
```sql
COMMIT;
```

**回滚事务**：
```sql
ROLLBACK;
```

### 十二、游标与存储过程

**创建游标**：
```sql
DECLARE 游标名 CURSOR FOR SELECT 列名 FROM 表名;
```

**打开游标**：
```sql
OPEN 游标名;
```

**获取游标数据**：
```sql
FETCH 游标名 INTO 变量名;
```

**关闭游标**：
```sql
CLOSE 游标名;
```

**创建存储过程**：
```sql
CREATE PROCEDURE 存储过程名 AS BEGIN ... END;
```

**调用存储过程**：
```sql
CALL 存储过程名();
```

### 十三、函数与触发器

**创建函数**：
```sql
CREATE FUNCTION 函数名() RETURNS 数据类型 AS BEGIN ... END;
```

**调用函数**：
```sql
SELECT 函数名();
```

**创建触发器**：
```sql
CREATE TRIGGER 触发器名 BEFORE INSERT ON 表名 FOR EACH ROW SET 新列 = '值';
```

**删除触发器**：
```sql
DROP TRIGGER 触发器名;
```

### 十四、系统信息查询

**查询当前用户**：
```sql
SELECT CURRENT_USER();
```

**查询当前数据库**：
```sql
SELECT DATABASE();
```

**查询表的行数和大小**：
```sql
SELECT TABLE_NAME, TABLE_ROWS, DATA_LENGTH FROM information_schema.TABLES WHERE TABLE_SCHEMA = '数据库名';
```

**获取表的创建时间**：
```sql
SELECT CREATE_TIME FROM information_schema.TABLES WHERE TABLE_NAME = '表名';
```

**获取表的修改时间**：
```sql
SELECT UPDATE_TIME FROM information_schema.TABLES WHERE TABLE_NAME = '表名';
```

### 十五、其他实用查询

**使用LIMIT与ORDER BY结合**：
```sql
SELECT * FROM 表名 ORDER BY 列名 LIMIT 10;
```

**查询表的外键约束**：
```sql
SELECT CONSTRAINT_NAME, TABLE_NAME FROM information_schema.KEY_COLUMN_USAGE WHERE TABLE_SCHEMA = '数据库名';
```

**查询表的主键约束**：
```sql
SELECT CONSTRAINT_NAME, TABLE_NAME FROM information_schema.TABLE_CONSTRAINTS WHERE TABLE_SCHEMA = '数据库名' AND CONSTRAINT_TYPE = 'PRIMARY KEY';
```

**使用ROLLUP进行分组汇总**：
```sql
SELECT 列名, SUM(列名2) FROM 表名 GROUP BY 列名 WITH ROLLUP;
```

**获取前N条记录**：
```sql
SELECT * FROM 表名 LIMIT N;
```

**获取最后N条记录**：
```sql
SELECT * FROM 表名 ORDER BY 列名 DESC LIMIT N;
```

**使用NOT EXISTS进行条件判断**：
```sql
SELECT * FROM 表名 WHERE NOT EXISTS (SELECT 1 FROM 其他表名 WHERE 条件);
```

**使用IN进行条件判断**：
```sql
SELECT * FROM 表名 WHERE 列名 IN (值1, 值2);
```

**使用NOT IN进行条件判断**：
```sql
SELECT * FROM 表名 WHERE 列名 NOT IN (值1, 值2);
```

**使用UNION ALL**：
```sql
SELECT 列名 FROM 表1 UNION ALL SELECT 列名 FROM 表2;
```

### 十六、性能优化

**使用EXPLAIN分析查询**：
```sql
EXPLAIN SELECT * FROM 表名 WHERE 条件;
```

**优化索引**：
```sql
CREATE INDEX 索引名 ON 表名 (列名);
```

**使用临时表**：
```sql
CREATE TEMPORARY TABLE 临时表名 AS SELECT * FROM 表名;
```

**查询表的索引**：
```sql
SHOW INDEX FROM 表名;
```

**查询数据库版本**：
```sql
SELECT VERSION();
```

### 十七、常见错误处理

**捕获错误**：
```sql
DECLARE CONTINUE HANDLER FOR SQLEXCEPTION BEGIN ... END;
```

**输出错误信息**：
```sql
SELECT ERROR_MESSAGE();
```

**使用事务处理错误**：
```sql
BEGIN; -- 开始事务
-- 执行SQL语句
-- 如果有错误，ROLLBACK
```

### 十八、数据备份与恢复

**备份数据库**：
```sql
mysqldump -u 用户名 -p 数据库名 > 备份文件.sql
```

**恢复数据库**：
```sql
mysql -u 用户名 -p 数据库名 < 备份文件.sql
```

### 十九、数据导入与导出

**导入数据**：
```sql
LOAD DATA INFILE '文件路径' INTO TABLE 表名;
```

**导出数据**：
```sql
SELECT * INTO OUTFILE '文件路径' FROM 表名;
```

### 二十、常用工具与命令

**显示当前数据库**：
```sql
SELECT DATABASE();
```

**显示所有数据库**：
```sql
SHOW DATABASES;
```

**显示所有表**：
```sql
SHOW TABLES;
```

**显示表结构**：
```sql
DESCRIBE 表名;
```

**显示当前连接信息**：
```sql
SHOW PROCESSLIST;
```

**显示数据库使用情况**：
```sql
SELECT table_schema AS '数据库', SUM(data_length + index_length) / 1024 / 1024 AS '大小(MB)' FROM information_schema.TABLES GROUP BY table_schema;
```

**显示表的行数**：
```sql
SELECT COUNT(*) FROM 表名;
```

**显示用户权限**：
```sql
SHOW GRANTS FOR '用户名'@'主机名';
```
