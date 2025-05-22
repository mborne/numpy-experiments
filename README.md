# numpy-experiment

Some basic examples to test [numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html), [matplotlib](https://matplotlib.org/index.html), [tensorflow](https://www.tensorflow.org/) and [pytorch].

## Usage

With [uv](https://github.com/astral-sh/uv#readme) :

```bash
# download dependencies
uv sync
# start jupyter notebook (should open browser)
uv run --with jupyter jupyter lab
```

## Notebooks

* [01-noisy-line.ipynb](01-noisy-line.ipynb) : Estimate line parameters using [numpy.linalg.lstsq](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.lstsq.html) (classical approach using matrix for linear equations)
* [04-circle-estimation-gradient.ipynb](04-circle-estimation-gradient.ipynb) : Estimate circle parameters using gradient descent with manual derivation (before testing autograd from pytorch).

## Old examples

> Not yet converted into jupyter notebooks

### 02-noisy-circle

Estimate circle using least squares with linearisation :

[02-noisy-circle.py](02-noisy-circle.py)

![data/noisy-circle.png](data/noisy-circle.png)

### 03-noisy-circle-tf

Estimate circle using gradient descent (`tf.keras.optimizers.SGD`) from tensorflow V2 :

[03-noisy-circle-tf.py](03-noisy-circle-tf.py)

![data/noisy-circle.png](data/noisy-circle.png)
