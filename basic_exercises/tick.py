import matplotlib.pyplot as plt
import numpy as np

# 生成等差数列
x = np.linspace(-3, 3, 50)
y = 0.1 * x

# figure类似一个画布，matplotlib画图都是基于figure的
plt.figure()
plt.plot(x, y, color='b', linewidth=10, linestyle='-')
plt.ylim([-2, 2])

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

# Get the xaxis' tick labels.
# https://blog.csdn.net/dss_dssssd/article/details/84567689
for label in ax.get_xticklabels() + ax.get_yticklabels():
    # 设置坐标轴上各个刻度的字体大小
    label.set_fontsize(16)
    # 设置各个刻度线上的边框样式， facecolor: 背景色
    # edegcolor: 边框的颜色 alpha: 透明度，当前为70%不透明
    label.set_bbox(dict(facecolor='white', edgecolor='g', alpha=0.7))

plt.show()
