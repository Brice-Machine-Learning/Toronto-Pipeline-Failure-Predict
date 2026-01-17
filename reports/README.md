# Reports

This directory contains the Quarto-based reporting system for the project.

## Requirements

- Quarto >= 1.8.x
- Python environment: `.venv-reports` (managed with uv)

## Render Reports

From the project root:

```bash
quarto render reports
```

This will generate the reports and place the output in the `reports/_site` directory.
