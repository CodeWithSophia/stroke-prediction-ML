# Stroke Prediction — Machine Learning Project

## Overview
This project builds an end-to-end machine learning system to predict the likelihood of a stroke based on clinical and demographic data. The project includes data analysis, model training, and a deployed interactive web application. Early stroke detection can significantly improve patient outcomes by enabling timely medical intervention.

## Problem Statement
Stroke is the second leading cause of death globally according to the World Health Organization. Millions of cases could be prevented with early risk identification. This project explores whether clinical features such as age, hypertension, heart disease, BMI, and glucose levels can be used to predict stroke risk in patients before it occurs.

## Dataset
- **Source:** [Kaggle - Stroke Prediction Dataset by fedesoriano](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- **Size:** 5,110 patients, 12 clinical features
- **Target variable:** `stroke` (1 = stroke occurred, 0 = no stroke)
- **Class distribution:** 4,861 non-stroke cases (95.1%) vs 249 stroke cases (4.9%)

## Key Features
| Feature | Description |
|---|---|
| age | Age of the patient |
| hypertension | Whether patient has hypertension (0 = No, 1 = Yes) |
| heart_disease | Whether patient has heart disease (0 = No, 1 = Yes) |
| avg_glucose_level | Average glucose level in blood |
| bmi | Body Mass Index |
| smoking_status | Smoking history of patient |
| work_type | Type of employment |
| ever_married | Marital status |

## EDA Findings
- Stroke cases represent only **4.9%** of the dataset — significant class imbalance handled using SMOTE
- Patients aged **40 and above** account for the majority of stroke cases
- Patients with hypertension are **3x more likely** to have a stroke
- Patients with heart disease are **4x more likely** to have a stroke
- High average glucose levels correlate with increased stroke risk
- Age was confirmed as the strongest single predictor with a correlation of 0.245

## Methodology
1. **Exploratory Data Analysis** — Investigated distributions, correlations and clinical patterns
2. **Data Cleaning** — Handled 201 missing BMI values using median imputation
3. **Feature Engineering** — Encoded categorical variables using label encoding and one-hot encoding
4. **Class Imbalance** — Applied SMOTE to balance stroke vs non-stroke cases in training data only
5. **Feature Scaling** — Applied StandardScaler to normalise feature ranges before modelling
6. **Modelling** — Trained and compared Logistic Regression and Random Forest classifiers
7. **Evaluation** — Prioritised Recall and AUC over accuracy due to clinical importance of catching true stroke cases
8. **Deployment** — Built and deployed interactive Streamlit web application

## Model Performance
| Model | Recall (Stroke) | AUC Score | Accuracy |
|---|---|---|---|
| Logistic Regression | 0.58 | 0.795 | 83% |
| Random Forest | 0.04 | 0.772 | 94% |

## Key Finding
Logistic Regression outperformed Random Forest for this task despite being a simpler model. This is a common finding in medical datasets where interpretability and recall matter more than raw accuracy. Random Forest achieved 94% accuracy by predominantly predicting no stroke — clinically dangerous behaviour in a screening tool.

## Feature Importance
Top predictors identified by the model:
1. **Age (2.03)** — strongest predictor, consistent with clinical literature
2. **Work Type** — acts as a proxy for age and lifestyle demographic
3. **Smoking Status** — former and current smokers carry elevated risk

## Live Demo

**[Try the Stroke Risk Prediction App](#)** — *(link coming soon)*

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Streamlit

## Project Structure
[GitHub](https://github.com/CodeWithSophia) | [Linkedin](www.linkedin.com/in/ibuchukwu-ezeah)
