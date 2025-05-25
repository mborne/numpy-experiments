# numpy-experiments

Some basic examples to test [numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html), [matplotlib](https://matplotlib.org/index.html) and [pytorch](https://pytorch.org/).

## Examples

* [01-noisy-line](01-noisy-line.ipynb) : Estimate line parameters using [numpy.linalg.lstsq](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.lstsq.html) (classical approach using linear algebra)
* [02-noisy-circle](02-noisy-circle.ipynb) : Estimate circle parameters using [numpy.linalg.lstsq](https://numpy.org/doc/2.1/reference/generated/numpy.linalg.lstsq.html) (same as 01-noisy-line except that linearization is required for non linear equations)
* [03-noisy-circle-gradient](03-noisy-circle-gradient.ipynb) : Estimate circle parameters using **gradient descent** with **symbolic differentiation** (before testing autograd from pytorch).
* [04-noisy-circle-autograd](04-noisy-circle-autograd.ipynb) : Estimate circle parameters using **gradient descent** with **autograd** from pytorch.


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
