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
from RafayKhan.utilities import *
from RafayKhan.LinearLayer import LinearLayer
from RafayKhan.ActivationLayer import SigmoidLayer

X = np.array( [ [0, 0],
                [0, 1],
                [1, 0],
                [1, 1] ] )

Y = np.array([ [0], [1], [1], [0] ])

'''
    X[:, 0]  =  [0 0 1 1]
    X[:, 1]     [0 1 0 1]

    "np.c_" concatenates data column-wise
    X_t = [ [0 0 0]
            [0 1 0]
            [1 0 0]
            [1 1 1] ]
'''
X_train = np.c_[ X, X[:, 0] * X[:, 1] ]
X_train = X_train.T

learning_rate = 1
epochs = 5000

np.random.seed(48) # set seed value so that the results are reproduceable

# (input)--> [Linear->Sigmoid] -->(output)
#------ LAYER-1 ----- define output layer that takes in training data
Z1 = LinearLayer(input_shape=X_train.shape, n_out=1, ini_type='plain')

A1 = SigmoidLayer(Z1.Z.shape)

costs = []
## ----------------------------  training ----------------------------
for epoch in range(epochs):
    # ------------------------- forward-prop -------------------------
    # z = W ⋅ X + b,      where X = X_train
    Z1.forward(X_train)
    # Ŷ = 1 / (1 + e^-z), where z = Z1.Z
    A1.forward(Z1.Z)

    # ---------------------- Compute Cost ----------------------------
    # cost = 1/2m Σ (Y - Ŷ)⋅^2, dŶ = -1 / m ⋅ (Y - Ŷ), where m = Y.shape[0]
    cost, dY_hat = compute_cost(Y=Y.T, Y_hat=A1.A)

    # print and store Costs every 100 iterations.
    if (epoch % 100) == 99:
        print("Cost at epoch#{}: {}".format(epoch, cost))
        costs.append(cost)

    # ------------------------- back-prop ----------------------------
    # dZ = dŶ ⋅ Ŷ ⋅ (1 - Ŷ)
    A1.backward(dY_hat)
    # dZ / dW = X, db = db + dZ, Z(i-1) = Z(i)
    Z1.backward(A1.dZ)

    # ----------------------- Update weights and bias ----------------
    # W = W - α ⋅ W, b = b - α ⋅ b
    Z1.update_params(learning_rate=learning_rate)

## ----------------- see the ouptput predictions -------------------------
# z = w1⋅x1 + w2⋅x2 + b,
# σ(z) = 1 / (1 + e^-z)
# Ŷ = 1 if σ(z) > 0.5 else 0
predicted_outputs, _, accuracy = predict(X=X_train, Y=Y.T, Zs=[Z1], As=[A1])

print("The predicted outputs:\n {}".format(predicted_outputs))
print("The accuracy of the model is: {}%".format(accuracy))
plot_learning_curve(costs=costs, learning_rate=learning_rate, total_epochs=epochs)
plot_decision_boundary(lambda x:predict_dec(Zs=[Z1], As=[A1], X=x.T), X, Y, feat_crosses=[(0,1)])

print('OK!')
