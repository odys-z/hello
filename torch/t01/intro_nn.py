'''
https://pytorch.org/tutorials/beginner/nn_tutorial.html
'''
from pathlib import Path
import requests         # pip install requests (certifi)
import pickle
import gzip
from matplotlib import pyplot
import numpy as np
import torch
import math
# from IPython.core.debugger import set_trace

DATA_PATH = Path(".")
PATH = DATA_PATH / "mnist"

PATH.mkdir(parents=True, exist_ok=True)

URL = "https://github.com/pytorch/tutorials/raw/master/_static/"
FILENAME = "mnist.pkl.gz"

if not (PATH / FILENAME).exists():
        content = requests.get(URL + FILENAME).content
        (PATH / FILENAME).open("wb").write(content)

with gzip.open((PATH / FILENAME).as_posix(), "rb") as f:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(f, encoding="latin-1")

x_train, y_train, x_valid, y_valid = map(
    torch.tensor, (x_train, y_train, x_valid, y_valid)
)
print(x_train.shape, y_train.shape, x_valid.shape, y_valid.shape)

xr, xc = 3, 4
f, ax = pyplot.subplots(xr, xc)
for r in range(xr):
    for c in range(xc):
        ax[r][c].imshow(x_train[r * xc + np.random.randint(100) + c].reshape((28, 28)), cmap="gray")
        ax[r][c].set_xticks([])
        ax[r][c].set_yticks([])
# pyplot.show()
pyplot.savefig('./rand-pic.png')

print(x_train.shape)

# ------------------------------ initializing ----------------------------------
weights = torch.randn(784, 10) / math.sqrt(784)  # @UndefinedVariable
weights.requires_grad_()
bias = torch.zeros(10, requires_grad=True)       # @UndefinedVariable

# forward
def log_softmax(x):
    return x - x.exp().sum(-1).log().unsqueeze(-1)

def model(xb):
    return log_softmax(xb @ weights + bias)

def accuracy(out, yb):
    preds = torch.argmax(out, dim=1)  # @UndefinedVariable
    return (preds == yb).float().mean()

def nll(input, target):
    # [range(), p] is called fancy indexing by Aladdin Persson
    # https://www.youtube.com/watch?v=x9JiIFvlUwk&list=PLhhyoLH6IjfxeoooqP9rhU3HJIAVAJ3Vz&index=2
    # 36:30
    # input.shape == [64, 10], target = [y_0, ..., y_63]
    return -input[range(target.shape[0]), target].mean()

loss_func = nll

bs = 64
lr = 0.05   # learning rate
epochs = 2  # how many epochs to train for

# training
for epoch in range(epochs):
    for i in range((x_train.shape[0] - 1) // bs + 1):
        #         set_trace()
        i0, i1 = i * bs, (i+1) * bs
        Xi = x_train[i0 : i1]
        Yi = y_train[i0 : i1]
        Yi_h = model(Xi)
        loss = loss_func(Yi_h, Yi)

        loss.backward()
        with torch.no_grad():
            weights -= weights.grad * lr
            bias -= bias.grad * lr
            weights.grad.zero_()
            bias.grad.zero_()

#         print(loss, accuracy(Yi_h, Yi))
print(loss_func(model(Xi), Yi), accuracy(model(Xi), Yi))
