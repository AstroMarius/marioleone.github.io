---
layout: page
title: "Predictive Analytics with Machine Learning"
permalink: /projects/datascientist/
---
{% include project-code.html %}

<!-- markdownlint-disable MD025 MD022 MD032 -->

# 🤖 Predictive Analytics with Machine Learning

**Leveraging data to build predictive models.**
A project demonstrating how advanced **machine learning techniques** can be applied to financial and industrial datasets for forecasting and optimization.

## 🔹 Overview
The goal was to implement scalable ML workflows for **churn prediction**, **risk modeling**, and **time-series forecasting**, ensuring reproducibility and real-world deployment readiness.

## 🔹 Focus
- Data preprocessing and feature engineering
- Model training and evaluation (classification & regression)
- Hyperparameter tuning and performance optimization
- Integration of models into production pipelines

## 🔹 Tech Stack
- **Languages**: Python, R, SQL
- **ML/AI**: Scikit-learn, PyTorch, TensorFlow
- **Data**: Pandas, NumPy, ClickHouse
- **Ops**: Docker, GitHub Actions, Jupyter

## 🔹 Highlights
- Built a **gradient boosting model** achieving 85% accuracy in churn prediction
- Designed a **credit risk model** combining logistic regression and ML ensembles
- Implemented **LSTM models** for time-series trend forecasting

## 🔹 Outcome
Delivered **scalable predictive models** that provided actionable insights and improved decision-making in financial and industrial contexts.

## Link al Codice

[Repository GitHub](https://github.com/AstroMarius/datascientist-ml-project){:target="_blank" rel="noopener"}

Clone (SSH): `git clone git@github.com:AstroMarius/datascientist-ml-project.git`

## 🔹 Esempio di Codice

```python
import pandas as pd
import matplotlib.pyplot as plt

# Caricamento del dataset
data = pd.read_csv('data/sales.csv', parse_dates=['date'])
data['sales'].plot()
plt.title('Andamento vendite nel tempo')
plt.show()
```

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Preparazione dei dati
X = data.drop(['date', 'sales'], axis=1)
y = data['sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Addestramento del modello
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
preds = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, preds):.2f}")
```
