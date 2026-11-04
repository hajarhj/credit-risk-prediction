# Credit Risk Prediction Using Machine Learning

## Overview

This project focuses on credit risk prediction using machine learning algorithms. The objective is to build a structured Python application that processes credit data, trains classification models, and evaluates their performance.

The project also applies software engineering best practices, including modular programming, object-oriented design, and code quality tools.

## Machine Learning Models

Two classification algorithms are implemented:

- **Logistic Regression**
- **Random Forest Classifier**

The project allows model training, evaluation, and prediction.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- Ruff
- Black
- Git and GitHub

## Project Structure

```text
credit_project/
├── data/
│   └── raw/
│       └── credit.csv
├── docs/
├── models/
├── notebooks/
│   └── exploration.ipynb
├── src/
│   └── credit_risk/
│       ├── __init__.py
│       ├── data.py
│       ├── evaluation.py
│       ├── logistic_regression_trainer.py
│       ├── model_trainer.py
│       ├── prediction.py
│       ├── preprocessing.py
│       ├── random_forest_trainer.py
│       └── training.py
├── tests/
├── main.py
├── pyproject.toml
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/hajarhj/credit-risk-prediction.git
cd credit-risk-prediction
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib jupyter black ruff
```

## Run the Project

Execute the main application:

```bash
python main.py
```

## Project Objectives

- Organize a machine learning project using a modular architecture.
- Prepare and preprocess credit datasets.
- Train and compare classification algorithms.
- Evaluate model performance.
- Apply Python code quality standards.
- Improve maintainability and reusability.

## Author

Hajar — Machine Learning & Data Science Project
