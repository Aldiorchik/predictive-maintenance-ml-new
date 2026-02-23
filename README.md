Predictive Maintenance System

Production-ready ML system for predicting aircraft engine failure risk using sensor data.

Problem

Aircraft engines degrade over time and may fail unexpectedly.
Unexpected failure leads to:

high maintenance costs

operational downtime

safety risks

The goal is to predict engine failure risk in advance using historical sensor data.

Dataset used: NASA CMAPSS (FD001 subset)
Task: Predict Remaining Useful Life (RUL) and classify failure risk.

Modeling Approach
Feature Engineering

To capture engine degradation patterns, the following techniques were applied:

Rolling mean smoothing

Lag features

Cycle normalization

RUL capping to reduce variance

These transformations help the model learn temporal degradation trends rather than raw noisy sensor values.

Models Used

Linear Regression (baseline)

RandomForestClassifier

Gradient Boosting (experimented)

RandomForest showed the best stability and generalization performance.

Results

MAE improved from 27 → 12 after feature engineering

ROC-AUC: [insert your value]

Precision / Recall: [insert your values]

Feature importance analysis revealed the most critical sensors influencing degradation.

System Architecture
User → Streamlit UI → FastAPI → ML Model

Streamlit handles user input

FastAPI serves the trained model

The model predicts failure risk and probability score

Results are visualized with confidence metrics and feature importance

Tech Stack

Python

Scikit-learn

Pandas / NumPy

FastAPI

Streamlit

Matplotlib / Seaborn
