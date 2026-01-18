# Project Structure for Pipeline Break Prediction

```plaintext
pipeline_failure_predict/
├── README.md                   # Project overview and instructions
├── pyproject.toml              # Python project configuration file
├── requirements.txt            # Python dependencies file
├── environment.yml             # Conda environment file
├── .gitignore                  # Git ignore file
├── .env.example                # Example environment variables file
├── .env                        # Environment variables file (not included in version control)
├── data/                       # Data directory
│   ├── raw/
│   │   ├── climate/
│   │   ├── gis/
│   │   ├── soils/
│   │   └── watermain_breaks/
│   │       └── pipeline_breaks.csv
│   ├── interim/
│   │   ├── climate/
│   │   ├── gis/
│   │   ├── soils/
│   │   ├── watermain_data/
│   │   └── watermain_breaks/
│   ├── processed/
│   │   ├── climate/
│   │   ├── gis/
│   │   ├── soils/
│   │   ├── watermain_data/
│   │   └── watermain_breaks/
│   └── external/
│       └── soils_layers/
│
├── notebooks/                                      # Jupyter notebooks
│   ├── 00_baseline/                                # Baseline Analysis
│   │   └── 00_problem_framing.ipynb
│   ├── 01_eda/                                     # Exploratory Data Analysis
│   │   ├── 01_eda_watermain_breaks.ipynb
│   │   ├── 02_eda_watermain_data.ipynb
│   │   ├── 03_eda_soil_data.ipynb
│   │   ├── 04_eda_climate_data.ipynb
│   │   └── 99_eda_summary.ipynb
│   ├── 02_feature_engineering/                     # Feature Engineering
│   │   ├── 01_features_spatial_aggregation.ipynb
│   │   ├── 02_features_temporal_aggregation.ipynb
│   │   └── 03_features_joined_table.ipynb
│   ├── 03_model_training/                          # Model Training
│   │   ├── 01_baseline_poisson.ipynb
│   │   └── 02_logistic_regression.ipynb
│   ├── 04_evaluation/                              # Model Evaluation
│   │   ├── 01_evaluation_metrics.ipynb
│   │   └── 02_error_analysis.ipynb
│   └── 05_risk_scoring/                            # Risk Scoring
│       ├── 01_risk_score_calculation.ipynb
│       └── 02_risk_maps.ipynb
│
├── schemas/                        # Schema definitions
│   ├── features_schema.yaml
│   ├── model_schema.yaml
│   ├── data_schema.yaml
│   ├── risk_score_schema.yaml
│   └── powerbi_export_schema.yaml
│
├── powerbi/                        # Power BI project files
│   ├── README.md
│   ├── datasets/
│   │   ├── pipe_breaks.sql
│   │   ├── climate_monthly.sql
│   │   └── joined_risk_view.sql
│   ├── model/
│   │   ├── relationships.md
│   │   ├── measures.md
│   │   └── pipeline_failure_model.pbix
│   ├── reports/
│   │   ├── pipeline_failure_overview.pbix
│   │   ├── pipeline_failure_risk.pbix
│   │   └── pipeline_failure_dashboard.pbix
│   └── exports/
│       ├── powerbi_export.sql
│       ├── data_validation_checks.md
│       └── refresh_notes.md
│
├── src/pipeline_failure_predict/       # Source code directory
│   ├── __init__.py
│   ├── api/                            # API clients
│   │   └── pipeline_failure_client.py
│   ├── auth/                           # Authentication clients
│   │   └── pipeline_failure_auth.py
│   ├── config/                         # Configuration files
│   │   └── settings.py
│   ├── core/
│   │   └── __init__.py
│   ├── data/                           # Data handling
│   │   ├── download.py
│   │   ├── make_dataset.py
│   │   └── geospatial_utils.py
│   ├── db/                             # Database interaction
│   │   ├── __init__.py
│   │   ├── connection.py
│   │   ├── session.py                  # optional helper
│   │   ├── migrations/
│   │   │   ├── 01_create_tables.sql
│   │   │   └── 02_add_indexes.sql
│   │   └── queries/
│   │       ├── pipe_breaks.sql
│   │       ├── features.sql
│   │       └── risk_scores.sql
│   ├── etl/                            # ETL processes
│   │   └── ingest_breaks.py
│   ├── features/                       # Feature engineering
│   │   └── build_features.py
│   ├── log/                            # Logging utilities
│   │   └── logger.py
│   ├── models/                         # Modeling
│   │   ├── train_model.py
│   │   ├── predict_model.py
│   │   └── evaluate_model.py
│   ├── static/                         # Static files
│   │   └── __init__.py
│   ├── templates/                      # Template files
│   │   ├── base.html
│   │   ├── base_auth.html              # Base template for authentication pages
│   │   ├── base_dashboard.html         # Base template for dashboard pages (with sidebar)
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   └── register.html
│   │   ├── dashboard/
│   │   │   ├── dashboard.html
│   │   │   ├── onboarding.html         # Onboarding page (for new users)
│   │   │   └── profile.html
│   │   ├── reports/
│   │   │   ├── report_overview.html    # Report overview template (list of reports)
│   │   │   ├── risk_assessment.html    # Risk assessment report template (detailed)
│   │   │   └── risk_report.html        # Power BI report 
│   │   ├── partials/
│   │   │   ├── navbar.html             # Navigation bar partial
│   │   │   ├── sidebar.html            # Sidebar partial
│   │   │   ├── flash_messages.html     # Flash messages partial
│   │   │   ├── breadcrumbs.html        # Breadcrumbs partial (navigation aid)
│   │   │   ├── powerbi_embed.html      # Power BI embed partial (for embedding reports)
│   │   │   └── footer.html             # Footer partial
│   │   └── errors/
│   │       ├── 404.html
│   │       └── 500.html
│   ├── visualization/                  # Visualization scripts
│   │   ├── __init__.py
│   │   ├── eda_plots.py
│   │   ├── feature_plots.py
│   │   └── risk_map.py
│   └── utils/                          # Utility functions
│       └── __init__.py
│
├── artifacts/                             # Trained models and artifacts directory
│   ├── trained/
│   └── model_registry.json
│
├── reports/                            # Reports directory (see 01a_structure_reports.md for details)
│
└── docs/                               # Documentation directory
    ├── 00_overview/
    │   ├── 00_project_overview.md
    │   └── 01_water_main_break_analytics.md
    │
    ├── 01_architecture/
    │   ├── 00_introduction.md
    │   ├── 01_structure.md
    │   ├── 02_data_flow.md
    │   └── 03_component_descriptions.md
    │
    ├── 02_data_sources/
    │   └── 01_pipe_break_data_sources.md
    │
    ├── 03_notebooks/
    │   
    ├── 04_reports/
    │   
    ├── 05_powerbi/
    │   └── 00_powerbi_dataset_requirements.md
    │ 
    ├── 06_database/
    │ 
    ├── 07_models/
    │ 
    ├── 08_deployment/
    │  
    ├── 09_security/  
    │   
    ├── 10_operations/
    │   
    ├── 11_project_diary_notes/
    │   
    ├── 12_future_plans/
    │ 
    ├── 13_lessons_learned/
    │   
    ├── 14_risk_scoring/
    │ 
    └── 15_medium_blog/        
```

## Description of Project Structure

This structure is designed to facilitate the development, maintenance, and collaboration on the Pipeline Break Prediction project. Each directory serves a specific purpose, ensuring that code, data, documentation, and reports are organized logically.

- `pipeline_failure_predict/`: Root directory of the project.
- `README.md`: Overview and instructions for the project.
- `pyproject.toml`, `requirements.txt`, and `environment.yml`: Dependency management files.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `.env.example`: Example environment variables file for configuration.
- `data/`: Contains raw, interim, processed, and external datasets.
- `notebooks/`: Jupyter notebooks for exploratory data analysis, feature engineering, model training, evaluation, and risk scoring.
- `schemas/`: YAML schema files defining the structure of features, models, data, risk scores, and Power BI exports.
- `powerbi/`: Power BI project files including datasets, models, reports, and export notes.
- `src/`: Source code for data processing, feature engineering, modeling, visualization, and utility functions.
- `src/pipeline_failure_predict/`: Main package for the project containing submodules for different functionalities.
- `src/pipeline_failure_predict/api/`: API client for interacting with Los Angeles data services.
- `src/pipeline_failure_predict/config/`: Configuration settings for the project.
- `src/pipeline_failure_predict/core/`: Core functionalities and initializations.
- `src/pipeline_failure_predict/data/`: Data handling and geospatial utilities.
- `src/pipeline_failure_predict/db/`: Database connection and query management.
- `src/pipeline_failure_predict/etl/`: Extract, Transform, Load processes for data ingestion.
- `src/pipeline_failure_predict/features/`: Feature engineering scripts.
- `src/pipeline_failure_predict/log/`: Logging utilities.
- `src/pipeline_failure_predict/models/`: Model training, prediction, and evaluation scripts.
- `src/pipeline_failure_predict/static/`: Static files for the project.
- `src/pipeline_failure_predict/templates/`: Template files for the project.
- `src/pipeline_failure_predict/visualization/`: Visualization scripts for EDA, features, and risk mapping.
- `src/pipeline_failure_predict/utils/`: Utility functions.
- `artifacts/`: Storage for trained models and model registry.
- `reports/`: Generated reports and figures for analysis and documentation.
- `docs/`: Documentation related to the project architecture and other relevant topics.
