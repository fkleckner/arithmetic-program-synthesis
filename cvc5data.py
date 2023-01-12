import matplotlib.pyplot as plt
import numpy as np

x_axis = np.array([2, 3, 4, 5])
in_ms = [13, 79, 2692, 461793]
for num in in_ms:
	num = num * 0.001

y_axis = np.array(in_ms)


plt.scatter(x_axis, y_axis)
plt.show()