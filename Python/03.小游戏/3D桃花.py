# 导入必要的库
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建图形和3D坐标轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 定义网格和其他计算变量
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 6 * np.pi - 4*np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
change = np.sin(10*t)/20
u = 1 - (1 - np.mod(5.2 * t, 2 * np.pi) / np.pi) ** 4 / 2 + change
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p)) * 1.5
h = u * (x * np.cos(p) - y * np.sin(p))

# 设置颜色映射
c = plt.get_cmap('spring_r')

# 绘制3D曲面
ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1, cmap=c, linewidth=0, antialiased=True)

# 显示图形
plt.show()
