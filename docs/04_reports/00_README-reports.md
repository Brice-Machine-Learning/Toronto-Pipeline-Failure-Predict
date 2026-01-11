# Reports Environment

Reports are rendered using Quarto and a dedicated uv environment:

- Environment: `.venv-reports`
- Managed with: `uv`
- Purpose: offline report rendering only

This environment is intentionally separate from:

- Conda ML environments
- Deployment environments
