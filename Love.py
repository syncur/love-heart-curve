"""
import numpy as np
import matplotlib.pyplot as plt
a = 520
t = np.linspace(0, 2*np.pi, 100)
x = a*(2*np.cos(t)-np.cos(2*t))
y = a*(2*np.sin(t)-np.sin(2*t))
plt.plot(y, x, color='r')
plt.show()

"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-50, 50, 1)
y = np.arange(-50, 50, 1)
x, y = np.meshgrid(x, y)

f = 21*pow(x, 2)+21*pow(y, 2)-21*np.abs(x)*y-221
# f = np.abs(x) + np.abs(y) - 1


plt.figure()
# plt.contour(x, y, f, color='r')
plt.contourf(x, y, f, 10, alpha=0.75, cmap=plt.cm.hot)
# 填充颜色 10表示按照高度分成10层 alpha表示透明度 cmap表示渐变标准,paired/hot

plt.show()





