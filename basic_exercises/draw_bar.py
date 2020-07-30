import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(12)
'''
功能：从一个均匀分布[low,high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.

参数介绍:
    
    low: 采样下界，float类型，默认值为0；
    high: 采样上界，float类型，默认值为1；
    size: 输出样本数目，为int或元组(tuple)类型，例如，size=(m,n,k), 则输出m*n*k个样本，缺省时输出1个值。
'''
Y1 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)

# 绘制条形图
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y in zip(X, Y1):
    print(x, y)
    plt.text(x + 0.04, +y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x, y in zip(X, Y2):
    plt.text(x + 0.04, -y - 0.05, '%.2f' % y, ha='center', va='top')

plt.xlim(-.5, n)
plt.xticks(())
plt.ylim(-1.5, 1.5)
plt.yticks(())
plt.show()
