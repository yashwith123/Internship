# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 11:36:09 2026

@author: yashwith de
"""

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



data = {
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Education_Level": ["Bachelors","Masters","PhD","PhD","Bachelors","Masters",
                        "PhD","Masters","Bachelors","Masters","Bachelors","PhD"],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000]
}

df = pd.DataFrame(data)

print("\nDataset Info:")
print(df.info())

target = "Salary"

numerical_cols = ["Age", "Experience"]
categorical_cols = ["Education_Level", "Department"]

le = LabelEncoder()
df["Education_Level_Encoded"] = le.fit_transform(df["Education_Level"])

df = pd.get_dummies(df, columns=["Department"], drop_first=True)

df = df.drop("Education_Level", axis=1)

print("\nDataset after encoding:")
print(df.head())


X = df.drop(target, axis=1)
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)
baseline_preds = model.predict(X_test)

baseline_score = r2_score(y_test, baseline_preds)
print("\nBaseline Model R² Score:", baseline_score)


# Standard Scaling (mean=0, std=1)
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model on scaled features
scaled_model = LinearRegression()
scaled_model.fit(X_train_scaled, y_train)
scaled_preds = scaled_model.predict(X_test_scaled)

scaled_score = r2_score(y_test, scaled_preds)
print("Model Score After Scaling:", scaled_score)

# TOPIC 4 — POLYNOMIAL FEATURES (Non-linear relationships)
poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Train model on engineered features
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
poly_preds = poly_model.predict(X_test_poly)

poly_score = r2_score(y_test, poly_preds)
print("Model Score After Polynomial Features:", poly_score)

print("\n===== PERFORMANCE COMPARISON =====")
print("Before Feature Engineering :", baseline_score)
print("After Scaling             :", scaled_score)
print("After Polynomial Features :", poly_score)


print("\nFinal Feature Shape:", X_train_poly.shape)

print("\nFeature Engineering Completed Successfully!")