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

## View Reports

Open the generated HTML files in the `reports/_site` directory using a web browser to view the reports.
For example, to open the main report:

```bash
open reports/_site/index.html
```

or on Linux:

```bash
xdg-open reports/_site/index.html
```

## View Preview

To preview the reports locally, you can use Quarto's preview feature:

```bash
quarto preview reports
```

This will start a local server and open the reports in your default web browser. Any changes made to the report files will automatically refresh the preview.
Press `Ctrl+C` in the terminal to stop the preview server when done.
