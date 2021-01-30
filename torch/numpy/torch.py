'''
    https://pytorch.org/tutorials/beginner/pytorch_with_examples.html
'''
# -*- coding: utf-8 -*-
import numpy as np
import math
import matplotlib.pyplot as plt

# Create random input and output data
epochs = 80
x = np.linspace(-math.pi, math.pi, epochs)
y = np.sin(x)

# Randomly initialize weights
a = np.random.randn()
b = np.random.randn()
c = np.random.randn()
d = np.random.randn()

learning_rate = 1e-6
loss = [0] * epochs
y_hat = [0] * epochs

for t in range(epochs):
    # Forward pass: compute predicted y
    # y = a + b x + c x^2 + d x^3
    y_hat[t] = a + b * x + c * x ** 2 + d * x ** 3

    # Compute and print loss
    loss[t] = np.square(y_hat[t] - y).sum()
    if t % 100 == 99:
        print(t, loss[t], y_hat[t])

    # Backprop to compute gradients of a, b, c, d with respect to loss
    # ∂L / ∂Ŷ
    grad_y_pred = 2.0 * (y_hat[t] - y)
    # ∂L / ∂a =  ∂L / ∂Ŷ ⋅ ∂Ŷ / ∂a = ∂L / ∂Ŷ ⋅ a
    grad_a = grad_y_pred.sum()
    # ∂L / ∂b =  ∂L / ∂Ŷ ⋅ ∂Ŷ / ∂b = ∂L / ∂Ŷ ⋅ b
    grad_b = (grad_y_pred * x).sum()
    # ∂L / ∂c =  ∂L / ∂Ŷ ⋅ ∂Ŷ / ∂c = ∂L / ∂Ŷ ⋅ c
    grad_c = (grad_y_pred * x ** 2).sum()
    # ∂L / ∂d =  ∂L / ∂Ŷ ⋅ ∂Ŷ / ∂d = ∂L / ∂Ŷ ⋅ d
    grad_d = (grad_y_pred * x ** 3).sum()

    # Update weights
    a -= learning_rate * grad_a
    b -= learning_rate * grad_b
    c -= learning_rate * grad_c
    d -= learning_rate * grad_d

print(f'Result: y = {a} + {b} x + {c} x^2 + {d} x^3')

fig, al = plt.subplots()
fig.canvas.set_window_title("Ŷ = a + b⋅x + c⋅x^2 + d⋅x^3")
ay = al.twinx()
ay.plot(x, y_hat, 'r', label='Ŷ')
ay.plot(x, y, lw=0.4, label='')
al.plot(x, loss, 'b-.', lw=0.4, label='Loss')

plt.show()
