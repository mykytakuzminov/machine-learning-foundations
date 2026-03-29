# Python LinLag Core
[![CI](https://github.com/mykytakuzminov/python-linlag-core/actions/workflows/ci.yml/badge.svg)](https://github.com/mykytakuzminov/python-linlag-core/actions)
![Python](https://img.shields.io/badge/python-3.14-3776ab?logo=python&logoColor=white)
![uv](https://img.shields.io/badge/uv-package%20manager-de5fe9)
![mypy](https://img.shields.io/badge/mypy-strict-2a6db5)
![ruff](https://img.shields.io/badge/ruff-linter-d7ff64?logoColor=black)
![tox](https://img.shields.io/badge/tox-automation-ce3262?logo=python&logoColor=white)

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
