import matplotlib.pyplot as plt
import numpy as np

'''
loc:float

　　概率分布的均值，对应着整个分布的中心center

　　scale:float

　　概率分布的标准差，对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高

　　size:int or tuple of ints

　　输出的shape，默认为None，只输出一个值

　　我们更经常会用到np.random.randn(size)所谓标准正太分布（μ=0, σ=1），对应于np.random.normal(loc=0, scale=1, size)
'''
n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)
# 绘制散点图
'''
s: 散点的大小
以平方磅为单位的标记面积，指定为下列形式之一：
数值标量 ： 以相同的大小绘制所有标记。
行或列向量 ： 使每个标记具有不同的大小。x、y 和 sz 中的相应元素确定每个标记的位置和面积。sz 的长度必须等于 x 和 y 的长度。
[] ： 使用 36 平方磅的默认面积。
'''
plt.scatter(X, Y, s=75, c=T, alpha=0.5)
plt.ylim([-2, 2])

plt.show()
