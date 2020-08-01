import matplotlib.pyplot as plt
import numpy as np


def f(x, y):

    # exp，高等数学里以自然常数e为底的指数函数
    return (1 - x/2 + x**5 + y**3)*np.exp(-x**2 - y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

# https://www.cnblogs.com/shenxiaolin/p/8854197.html
# https://blog.csdn.net/abc13526222160/article/details/88559162
# meshgrid函数通常使用在数据的矢量化上。
# 它适用于生成网格型数据，可以接受两个一维数组生成两个二维矩阵，对应两个数组中所有的(x,y)对。
X, Y = np.meshgrid(x, y)

# 给等高线图绘制不同的颜色
plt.contourf(X, Y, f(X, Y), 10, alpha=0.75, cmap=plt.cm.hot)

# 使用plt.contour 添加等高线线条
C = plt.contour(X, Y, f(X, Y), 10, colors='black')
# 添加标签
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()
