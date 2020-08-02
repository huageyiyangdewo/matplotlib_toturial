import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


fig, ax1 = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)

line, = ax1.plot(x, np.sin(x))


def animate(i):
    line.set_ydata(np.sin(x+i/20))
    return line,


def init():
    line.set_ydata(np.sin(x))
    return line,


ani = animation.FuncAnimation(
    fig=fig,
    func=animate,
    frames=100,
    init_func=init,
    interval=20,
    blit=True
)
#
# ani = animation.FuncAnimation(
#     fig=fig,
#     func=lambda i: line.set_ydata(np.sin(x+i/20)),
#     frames=100,
#     init_func=lambda i: line.set_ydata(np.sin(x)),
#     interval=20,
#     blit=True
# )

plt.show()