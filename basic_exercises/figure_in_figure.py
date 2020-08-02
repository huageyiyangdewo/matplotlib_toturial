import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6]
y = [1, 3, 4, 5, 6, 9]

fig = plt.figure()
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# 距离左边框的比例， 距离下边框的比例， 宽度、长度的比例
ax1 = fig.add_axes([left, bottom, width, height])
ax1.plot(x, y, 'r')
ax1.set_title('ax1')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

left, bottom, width, height = 0.15, 0.55, 0.3, 0.3
ax2 = fig.add_axes([left, bottom, width, height])
ax2.plot(x, y, 'g')
ax2.set_title('figure inside 1')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.axes([0.55, 0.15, 0.2, 0.2])
plt.plot(y[::-1], x, 'y')
plt.title('figure inside 2')
plt.xlabel('x')
plt.ylabel('y')


plt.show()



print(x, y)