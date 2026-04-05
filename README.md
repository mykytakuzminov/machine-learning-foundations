# Python LinLag Core

![Python](https://img.shields.io/badge/Python-3B6D11?logo=python&logoColor=fff)
![Uv](https://img.shields.io/badge/Uv-D85A30?logo=uv&logoColor=fff)
![Mypy](https://img.shields.io/badge/Mypy-0C447C?logo=python&logoColor=fff)
![Ruff](https://img.shields.io/badge/Ruff-A32D2D?logo=ruff&logoColor=fff)
![Tox](https://img.shields.io/badge/Tox-3C3489?logo=python&logoColor=fff)
![Pytest](https://img.shields.io/badge/Pytest-085041?logo=pytest&logoColor=fff)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-185FA5?logo=github-actions&logoColor=fff)

> A minimal linear algebra library in pure Python — built with strict typing, clean architecture, and modern tooling.

## 📦 Matrix

| Method | Description |
|---|---|
| `zeros(rows, cols)` | Matrix filled with 0.0 |
| `ones(rows, cols)` | Matrix filled with 1.0 |
| `identity(n)` | n×n identity matrix |
| `transpose()` | Transposed matrix |
| `trace()` | Sum of diagonal elements |
| `det()` | Determinant via Laplace expansion |
| `submatrix(row, col)` | Matrix without given row and column |
| `copy()` | Deep copy |
| `total()` | Sum of all elements |
| `mean()` | Mean of all elements |
| `row(i)` | i-th row as a list |
| `col(j)` | j-th column as a list |
| `is_square()` | Check if matrix is square |
| `is_symmetric()` | Check if matrix is symmetric |

Supports `+`, `-`, `*`, `/`, `**`, `-` (unary), `==` with scalars and other matrices.

## 🛠️ Tech Stack

- **[python](https://www.python.org/)** — core language, 3.14 with the latest features
- **[uv](https://github.com/astral-sh/uv)** — blazing fast package and environment management
- **[mypy](http://mypy-lang.org/)** — strict static type checking across the entire codebase
- **[ruff](https://github.com/astral-sh/ruff)** — linting and formatting in one tool
- **[tox](https://tox.wiki/)** — automated testing across isolated environments
- **[pytest](https://docs.pytest.org/)** — 100% test coverage with fixtures
- **[github actions](https://github.com/features/actions)** — CI on every push and pull request

## 🚀 Getting Started
```bash
git clone https://github.com/mykytakuzminov/python-linlag-core.git
cd python-linlag-core
uv sync
uv run tox
```
