# 100 Days of Python

This repository holds my "100 Days of Python" practice projects — one folder per day containing small exercises, examples, or projects.

Goals
- Build small, incremental projects daily
- Keep each day self-contained with tests
- Practice reading/writing clean Python and using testing/CI

Quickstart
1. Clone the repo:
   ```bash
   git clone git@github.com:deviousluck/100-days-of-python.git
   cd 100-days-of-python
   ```
2. Create a virtualenv and install dev dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt
   pre-commit install
   ```
3. Run tests:
   ```bash
   pytest
   ```

Repository layout
- `days/day-XX/` — each day gets its own folder (e.g. `day-01`, `day-02`)
- `days/day-XX/README.md` — any notes about the day's project
- `days/day-XX/*.py` — source files
- `days/day-XX/test_*.py` — tests runnable by pytest

Naming conventions
- Use `day-01`, `day-02`, ... for folder names (2-digit zero-padded).
- File names should be lowercase, underscore-separated: `my_solution.py`, `test_my_solution.py`.

CI / Badges
- CI checks formatting/linting (pre-commit) and runs tests on push/PR.
- Add shields/badges here once CI is set up.

Contributing
See [CONTRIBUTING.md](./CONTRIBUTING.md) for coding standards, PR process, and how to run tests locally.

License
This project is licensed under the MIT License — see LICENSE.