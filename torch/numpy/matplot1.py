'''
    https://www.kdnuggets.com/2019/08/numpy-neural-networks-computational-graphs.html

    neuron
    z = w1⋅x1 + w2⋅x2 + b,
    σ(z) = 1 / (1 + e^-z)

    ∂L / ∂ŷ = ∂(1/2(ŷ - y)^2) / ∂ŷ = -(y - ŷ)
    dŷ / dz = ŷ⋅(1 - ŷ)  =>  ∂L / ∂z = (∂L / ∂ŷ)⋅(∂ŷ / ∂z)
    ∂L / ∂w1 = (∂L / ∂z)⋅(∂z / ∂w1) = (∂L / ∂z)⋅x1
    ∂L / ∂w2 = (∂L / ∂z)⋅(∂z / ∂w2) = (∂L / ∂z)⋅x2
    ∂L / ∂b = 1

	Ci = 1/2m Σ (yi - ŷi)^2,  where i is i-th training example, Y = [y1, y2, ...]
    C(Y, Ŷ) = 1/2m Σ (Y - Ŷ)⋅^2
            = 1/2m [(y1 - ŷ1)^2, (y2 - ŷ2)^2, ...]
    ∂C/∂Ŷ = [∂C/ŷ1, ∂C/ŷ2, ...]
          = - 1/m [y1 - ŷ1, y2 - ŷ2, ...]
          = - 1/m (Y - Ŷ)
'''

import matplotlib.pyplot as plt
import numpy as np
from math import sin, pi

fig, ax = plt.subplots()  # Create a figure containing a single axes.
fig.canvas.set_window_title("plt.style.use('ggplot')")

s1 = np.linspace(0, 5*pi, 120)
s2 = [0] * len(s1)
s3 = [0] * len(s1)
for i in range(len(s2)):
    s2[i] = sin(s1[i])
    s3[i] = sin(s1[i] * pi * 0.1)


plt.style.use('ggplot')

ax.plot(s1, np.sinc(s1), label='np.sinc')
ax.plot(s1, s2, 'r-.', linewidth=.5, label='sin')
ax.plot(s1, s3, label='sin * 10', linewidth=.25)

plt.ylabel('y-Y')
plt.xlabel('... -- ...')
plt.legend()
plt.title('abc')
plt.grid(True)
plt.show()

print(plt.style.available)
print('OK!')
