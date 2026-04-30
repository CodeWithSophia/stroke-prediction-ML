# Stroke Prediction - Machine Learning Project

## Overview
This project builds a machine learning system to predict the likelihood of a stroke based on clinical and demographic data. Early stroke detection can significantly improve patient outcomes by enabling timely medical intervention.

## Problem Statement
Stroke is one of the leading causes of death and disability worldwide. This project explores whether clinical features such as age, hypertension, heart disease, BMI, and glucose levels can be used to predict stroke risk in patients.

## Dataset
- **Source:** [Kaggle - Stroke Prediction Dataset by fedesoriano](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Size:** 5,110 patients, 12 features
- **Target variable:** `stroke` (1 = stroke, 0 = no stroke)

## Key Features
| Feature | Description |
|---|---|
| age | Age of the patient |
| hypertension | 0 = No, 1 = Yes |
| heart_disease | 0 = No, 1 = Yes |
| avg_glucose_level | Average glucose level in blood |
| bmi | Body Mass Index |
| smoking_status | Smoking history of patient |

## EDA Findings
- Stroke cases represent only **4.9%** of the dataset — significant class imbalance
- Patients aged **40 and above** account for the majority of stroke cases
- Patients with hypertension are **3x more likely** to have a stroke
- Patients with heart disease are **4x more likely** to have a stroke

## Project Structure
```
stroke-prediction-ml/
│
├── stroke_prediction.ipynb    # Main notebook
├── healthcare-dataset-stroke-data.csv    # Dataset
└── README.md
```

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit (deployment)

## Status
**Work in Progress** — Currently at EDA and Data Cleaning stage

## Author
**Ibuchukwu Ezeah** | Deep Learning Engineer| 
[GitHub] (https://github.com/CodeWithSophia) | 
[LinkedIn] (https:www.linkedin.com/in/ibuchukwu-ezeah


