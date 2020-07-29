import matplotlib.pyplot as plt
import numpy as np

# 生成等差数列
x = np.linspace(-1, 1, 10)
y = x ** 2
y2 = 2 * x + 2

# figure类似一个画布，matplotlib画图都是基于figure的
plt.figure()
plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')
plt.plot(x, y2, color='black', linewidth=1.0, linestyle='-')

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


# gca: 获取当前图像的坐标系的四个边框
ax = plt.gca()

# 右边框、上边框消失掉
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 把下边框设置为x轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# 将下边框移动到y轴的0刻度处
# data还可以替换为axes、outward等
ax.spines['bottom'].set_position(('data', 1))
# 将左边框移动到x轴的0刻度处
ax.spines['left'].set_position(('data', 0))

plt.show()
