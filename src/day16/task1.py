# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 12:01:16 2026

@author: yashwith de
"""

# Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set(style="whitegrid")

# -----------------------------
# 1️⃣ Generate Datasets
# -----------------------------

np.random.seed(42)

# Normal Distribution (Human Heights)
heights = np.random.normal(loc=170, scale=10, size=1000)

# Right-Skewed Distribution (Household Income)
incomes = np.random.exponential(scale=50000, size=1000)

# Left-Skewed Distribution (Easy Test Scores)
scores = 100 - np.random.exponential(scale=15, size=1000)

# Create DataFrame
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})



def analyze_data(data, title):
    mean_value = np.mean(data)
    median_value = np.median(data)

    print(f"\n{title}")
    print("Mean   :", round(mean_value, 2))
    print("Median :", round(median_value, 2))

    if mean_value > median_value:
        print(" Right-Skewed Distribution")
    elif mean_value < median_value:
        print("Left-Skewed Distribution")
    else:
        print("Approximately Normal Distribution")

    # Plot Histogram with KDE
    plt.figure(figsize=(8,5))
    sns.histplot(data, kde=True, bins=30)
    plt.axvline(mean_value, color='red', linestyle='--', label='Mean')
    plt.axvline(median_value, color='green', linestyle='-', label='Median')
    plt.title(title)
    plt.legend()
    plt.show()

analyze_data(df["Heights"], "Human Heights (Normal Distribution)")
analyze_data(df["Incomes"], "Household Incomes (Right-Skewed)")
analyze_data(df["Scores"], "Test Scores - Easy Exam (Left-Skewed)")
