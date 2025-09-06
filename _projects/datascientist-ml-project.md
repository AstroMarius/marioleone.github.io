---
---
layout: project
title: "Data Scientist ML Project"
permalink: /projects/datascientist-ml-project/
---

## Data Scientist ML Project

## Introduzione

Questo progetto mira a risolvere il problema di previsione delle vendite future per un'azienda di e-commerce, utilizzando tecniche di Machine Learning per analizzare dati storici di transazioni e inventario.

## Problema

### Contesto

L'azienda soffriva di inefficienze nella gestione dell'inventario a causa di previsioni imprecise delle vendite mensili.

### Sfida

Il dataset conteneva valori mancanti, outlier e serie storiche con trend non lineari, rendendo difficile costruire modelli predittivi robusti.

## Approccio

### Analisi dei dati

Abbiamo esplorato il dataset con Pandas e Matplotlib per individuare anomalie:

```python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/sales.csv', parse_dates=['date'])
data['sales'].plot()
plt.title('Andamento vendite nel tempo')
plt.show()
```

### Feature Engineering e Modello

Dopo aver gestito dati mancanti e trasformazioni, abbiamo addestrato un modello Random Forest:
```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

X = data.drop(['date', 'sales'], axis=1)
y = data['sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f"MAE: {mean_absolute_error(y_test, predictions):.2f}")
```

## Risultati

- **MAE:** 12.34 (unità di vendita)
- Riduzione dell'errore di previsione del 25% rispetto al modello baseline.

## Tecnologie

- **Linguaggi:** Python
- **Librerie:** Pandas, Scikit-learn, Matplotlib
- **Strumenti:** Jupyter Notebook

## Conclusioni

### Lezioni Apprese

La fase di feature engineering e pulizia dei dati è stata cruciale per migliorare le performance del modello.

### Sviluppi Futuri

Integrare modelli di deep learning (LSTM) per catturare pattern temporali complessi.

## Link al Codice

[Repository GitHub](https://github.com/AstroMarius/datascientist-ml-project)
