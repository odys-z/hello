'''
https://pytorch.org/tutorials/beginner/nn_tutorial.html
'''
from pathlib import Path
import requests         # pip install requests (certifi)
import pickle
import gzip
from matplotlib import pyplot
import numpy as np

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

print(x_train.shape, y_train.shape, x_valid.shape, y_valid.shape)

xr, xc = 3, 4
f, ax = pyplot.subplots(xr, xc)
for r in range(xr):
    for c in range(xc):
        ax[r][c].imshow(x_train[r * xc + c].reshape((28, 28)), cmap="gray")
        ax[r][c].set_xticks([])
        ax[r][c].set_yticks([])
pyplot.show()

print(x_train.shape)
