# Contributor / Agent Guide – codex-hello-world

## Coding conventions
| Tool | Command |
|------|---------|
| **Black** | `black src tests` |
| **Ruff**  | `ruff check src tests` |

* The CI (GitHub Actions) will run `black --check` and `ruff --select F,E`.  
* All code **must** pass `pytest`.

## How to run locally

```bash
source .venv/bin/activate
black src tests
ruff check src tests
pytest
```
