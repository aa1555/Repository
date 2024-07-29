# 重新生成3D图形，根据用户提供的代码和注释

# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形和3D坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义网格，相位向后移动了6*pi
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 20 * np.pi + 4*np.pi)

# 计算p，添加边缘扰动
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
change = np.sin(15*t)/150

# 调整t的参数，使花瓣的角度变大
u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2 + change

# 计算y，r和h
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
h = u * (x * np.cos(p) - y * np.sin(p))

# 设置颜色映射
c = plt.get_cmap('Reds')

# 绘制3D曲面
ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1, cmap=c, linewidth=0, antialiased=True)

# 显示图形
plt.show()
