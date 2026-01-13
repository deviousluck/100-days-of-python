# Contributing

Thanks for contributing or following along!

Local setup
1. Create and activate a virtualenv:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Install dev dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
3. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

Code style
- Black for formatting
- isort for imports
- flake8 for linting

Testing
- Write pytest tests in files named `test_*.py`
- Run tests with `pytest`

Branching & PRs
- Create a branch for each change: `git checkout -b day-05/some-fix`
- Open PRs into `main`
- Keep PRs small and focused; include tests for bug fixes or new features

Commit messages
- Use short, present-tense prefixes, for example:
  - `feat: add day-10 solution`
  - `fix: correct off-by-one in day-03`
  - `chore: update dev dependencies`

Thanks — and enjoy the practice!