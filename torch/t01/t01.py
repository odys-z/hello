'''
	https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html
'''
from __future__ import print_function
import torch

x = torch.empty(5, 3)
print(x)

if torch.cuda.is_available():
    device = torch.device("cuda")          # a CUDA device object
    y = torch.ones_like(x, device=device)  # directly create a tensor on GPU
    x = x.to(device)                       # or just use strings ``.to("cuda")``
    z = x + y
    print(z)
    print(z.to("cpu", torch.double))

y = torch.ones_like(x)
print(y.size(), y, sep='\n')
