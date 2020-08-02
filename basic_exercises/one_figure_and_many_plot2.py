import matplotlib.pyplot as plt
from matplotlib import gridspec


fig = plt.figure()


def method1():
    # 使用subplot2grid绘制多个axes
    # 第一种在一个figure中画多个axes的方法
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
    ax1.plot([1, 2], [1, 2])
    # ax设置title、label、xlim等，比plt设置，前面多了set_
    ax1.set_title('ax1')

    ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2, rowspan=1)
    ax3 = plt.subplot2grid((3, 3), (1, 2), colspan=1, rowspan=2)
    ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=1, rowspan=1)
    ax5 = plt.subplot2grid((3, 3), (2, 1), colspan=1, rowspan=1)
    plt.show()


def method2():
    # 使用gridspec
    # 按照3行3列分割
    gs = gridspec.GridSpec(3, 3)
    ax1 = plt.subplot(gs[0, :])
    ax2 = plt.subplot(gs[1, :2])
    ax3 = plt.subplot(gs[1:, 2])
    ax4 = plt.subplot(gs[2, 0])
    ax5 = plt.subplot(gs[2, -2])
    plt.show()


def method3():
    # 使用subplots
    # sharex共享x轴
    f, ((ax11, ax12), (ax21, ax22)) = plt.subplots(2, 2, sharex=True, sharey=True)
    ax11.scatter([1, 2], [1, 2])
    ax12.scatter([1, 2], [1, 2])
    ax21.scatter([1, 2], [1, 2])
    ax22.scatter([1, 2], [1, 2])
    plt.show()


if __name__ == '__main__':
    # method1()
    # method2()
    method3()