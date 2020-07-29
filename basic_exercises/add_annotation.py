import matplotlib.pyplot as plt
import numpy as np

# 生成等差数列
x = np.linspace(-3, 3, 50)
y = 2 * x + 1

# figure类似一个画布，matplotlib画图都是基于figure的
plt.figure()
plt.plot(x, y, color='red', linewidth=1.0, linestyle='--')

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
ax.spines['bottom'].set_position(('data', 0))
# 将左边框移动到x轴的0刻度处
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1

# scatter: 绘制散点图
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=1.5)

# method 1
# https://blog.csdn.net/leaf_zizi/article/details/82886755
############################
plt.annotate(r'$2x=1=%s$' % y0, xy=(x0, y0), xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))

# method 2
##########################
plt.text(-2.7, 3, r'$this\ is\ test.\ \mu\ \sigma_i$',
         fontdict=dict(size=16, color='r'))
plt.show()
