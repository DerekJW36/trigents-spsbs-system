## Copilot / AI agent instructions (concise)

Purpose: give an AI coding agent the minimal, actionable knowledge to be immediately productive in this repo.

Notes about this workspace
- I couldn't find any existing agent docs (AGENT.md, .github/copilot-instructions.md, README.md) in the workspace. This file is written from sensible defaults for a Python projects workspace; please update any repo-specific paths or commands.

Big picture (what to look for)
- Typical layout: `src/` (application code) or top-level modules, `tests/` (pytest), `requirements.txt` or `pyproject.toml`, and optional `README.md`.
- If present, treat `src/` as authoritative for import paths (use `python -m` or install editable). If there is no `src/`, assume top-level package modules.

Developer workflows (commands to try)
- Create venv and install dependencies (PowerShell):
  - `python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt` (if `requirements.txt` exists)
  - `python -m pip install -e .` (if `pyproject.toml` / setup.cfg present and editable install is appropriate)
- Run tests (pytest): `pytest -q` (look for `tests/` directory)
- Lint/typecheck: look for `ruff`, `flake8`, or `mypy` in project files; run `ruff check .` or `mypy src` if configured.

Project-specific patterns and conventions to detect
- Packaging: prefer `pyproject.toml` (PEP 518) over `setup.py` if present.
- Imports: if there is an explicit `src/` dir, use that import layout when running tests and scripts (install editable mode to replicate CI).
- Config: environment variables often live in `.env` or `config/`. Check for `.env.example` or `settings.py`.

Integration points and external dependencies
- Search for keys like `requests`, `boto3`, `sqlalchemy`, `fastapi`, or `flask` in `requirements.txt` or `pyproject.toml` to detect external services.
- If you see `github/workflows` YAML, CI commands there are canonical for builds/tests.

How to be helpful as an AI editing this repo
- Always run the minimal local verification: create a venv, install deps (if available), and run a single failing or passing test to validate changes.
- When modifying imports or packaging, ensure tests still run both from `pytest` and with an editable install (`pip install -e .`) if packaging files exist.
- Prefer small, targeted edits with unit tests. If repo has no tests, add a minimal test that verifies behavior of your change.

Examples (update these to match the repository if different)
- If you modify application code in `src/myapp/`, add tests under `tests/test_myapp.py` and run `pytest tests/test_myapp.py::test_name -q` to check a single test.

If anything here is incorrect or you have repo-specific files, paste the top-level `tree` or list of files and I will merge/adjust these instructions.

Ask me to re-generate this after you add the repository files or point me to the key files to reference.
