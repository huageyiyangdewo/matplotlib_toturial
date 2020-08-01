import matplotlib.pyplot as plt
import numpy as np


# 等比数列
data = np.logspace(0.7, 0.3, 9, base=0.2).reshape((3, 3))

# https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.imshow.html
plt.imshow(data, interpolation='nearest', cmap='bone', origin='upper')
# shrink: 亚索比例
plt.colorbar(shrink=0.5)
plt.show()