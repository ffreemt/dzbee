# dzbee
[![pytest](https://github.com/ffreemt/dzbee/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/dzbee/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/dzbee.svg)](https://badge.fury.io/py/dzbee)

Align german(de)-chinese(zh) texts, fast

### Python 3.8 Only

## Pre-Install `fasttext`, `pycld2`, `PyICU`
*   If your computer **does not** have a C++ compiler,
 search for needed wheels at  https://www.lfd.uci.edu/~gohlke/pythonlibs/ and install, e.g.,
    ```
     pip install fasttext-0.9.2-cp38-cp38-win_amd64.whl pycld2-0.41-cp38-cp38-win_amd64.whl PyICU-2.8.1-cp38-cp38-win_amd64.whl
    ```
*   If your computer *does* have a C++ compiler
    ```
       pip insall fasttext pycld2 PyICU
       # poetry add fasttext pycld2 PyICU
    ```

## Install it

```shell
pip install dzbee

# poetry add dzbee
# pip install git+https://github.com/ffreemt/dzbee
# poetry add git+https://github.com/ffreemt/dzbee
# git clone https://github.com/ffreemt/dzbee && cd dzbee
```

## Use it
```bash
dzbee file1 file2

```
