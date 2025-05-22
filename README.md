# numpy-experiment

Some basic examples to test [numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html), [matplotlib](https://matplotlib.org/index.html), [tensorflow](https://www.tensorflow.org/) and [pytorch].

## Examples

* [01-noisy-line](01-noisy-line.ipynb) : Estimate line parameters using [numpy.linalg.lstsq](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.lstsq.html) (classical approach using matrix for linear equations)
* [02-noisy-circle](02-noisy-circle.ipynb) : Estimate circle parameters using [numpy.linalg.lstsq](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.lstsq.html) (same as 01-noisy-line except that linearization is required for non linear equations)
* [03-noisy-circle-tf.py](03-noisy-circle-tf.py) (**deprecated**) : Estimate circle using gradient descent (`tf.keras.optimizers.SGD`) from tensorflow V2
* [04-circle-estimation-gradient](04-circle-estimation-gradient.ipynb) : Estimate circle parameters using gradient descent with manual derivation (before testing autograd from pytorch).

## Usage

With [uv](https://github.com/astral-sh/uv#readme) :

```bash
# download dependencies
uv sync
# start jupyter notebook (should open browser)
uv run --with jupyter jupyter lab
```

## License

[MIT](LICENSE)
