'''
Try matplotlib

'''

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from Tools.demo.sortvisu import interpolate
import matplotlib.cm as cm

def fibonacci(n, generation):
    a, b = np.copy(n), np.copy(n)
    rabits = np.zeros((generation, n.size))

    for i in range(2, generation):
        rabits[i] = np.add(a, b)
        a, b = b, rabits[i]
    return rabits

def plot(histdata, row, col):
    h = plt.imshow(histdata, cmap='gist_ncar', interpolation='nearest')
    plt.axis('scaled')
    plt.colorbar()
    plt.show()

rabbits = np.array([1, 1, 3, 2, 4])

histdata = fibonacci(rabbits, 5)

print(histdata)

plot(histdata, 5, 5)
