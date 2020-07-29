import matplotlib.pyplot as plt
import numpy as np

# 生成等差数列
x = np.linspace(-1, 1, 10)
y = x ** 2
y2 = 2 * x + 2

# figure类似一个画布，matplotlib画图都是基于figure的
plt.figure()

# xlim、ylim 给x，y轴设置坐标轴的刻度
plt.xlim((-1, 1))
plt.ylim((0, 4))

# 给坐标轴给一个标签名
plt.xlabel('i am x')
plt.ylabel('i am y')

# 给坐标轴给定自定义的刻度
x_ticks = np.linspace(-1, 1, 4)
plt.xticks(x_ticks)

# 给坐标轴根据不同的值给不同的标识
plt.yticks([0, 1, 2.3, 3.1, 4],
           [r'$very\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$'])

# 设置handles时，l1后面的,不能少，否则报错
l1, = plt.plot(x, y, color='red', linewidth=1.0, linestyle='--', label='L1')
l2, = plt.plot(x, y2, color='black', linewidth=1.0, linestyle='-', label='L2')

# 设置图例 handles: 需要显示的图例  labels: 图例中线条的名称，优先级大于具体线条中的label
# loc: best, center, right等，也可以填数字，默认为best（自动找到一个尽量不遮挡图中数据的地方显示）
plt.legend(handles=(l1, l2), labels=['aaa', 'bbb'], loc='lower')
plt.show()
