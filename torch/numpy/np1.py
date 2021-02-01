'''
    https://www.kdnuggets.com/2019/08/numpy-neural-networks-computational-graphs.html

    neoro
    z = w1⋅x1 + w2⋅x2 + b,
    σ(z) = 1 / (1 + e^-z)

    ∂L / ∂ŷ = ∂(1/2(ŷ - y)^2) / ∂ŷ = -(y - ŷ)
    dŷ / dz = ŷ⋅(1 - ŷ)  =>  ∂L / ∂z = (∂L / ∂ŷ)⋅(∂ŷ / ∂z)
    ∂L / ∂w1 = (∂L / ∂z)⋅(∂z / ∂w1) = (∂L / ∂z)⋅x1
    ∂L / ∂w2 = (∂L / ∂z)⋅(∂z / ∂w2) = (∂L / ∂z)⋅x2
    ∂L / ∂b = 1

	Ci = 1/2m Σ (yi - ŷi)^2
'''

import numpy
