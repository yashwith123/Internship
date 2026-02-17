# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 12:07:43 2026

@author: yashwith de
"""
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Price": [200000, 220000, 250000, 270000, 300000, 320000, 350000,
              370000, 400000, 450000, 480000, 500000, 550000, 600000,
              650000, 700000, 750000, 800000, 900000, 1000000],
    
    "City": ["Bangalore", "Mumbai", "Delhi", "Bangalore", "Chennai",
             "Mumbai", "Delhi", "Bangalore", "Chennai", "Delhi",
             "Mumbai", "Bangalore", "Chennai", "Delhi", "Mumbai",
             "Bangalore", "Chennai", "Delhi", "Mumbai", "Bangalore"]
}

df = pd.DataFrame(data)


plt.figure(figsize=(6,4))
sns.histplot(df['Price'], kde=True)
plt.title("Price Distribution with KDE")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()


skewness = df['Price'].skew()
kurtosis = df['Price'].kurt()

print("Skewness of Price:", skewness)
print("Kurtosis of Price:", kurtosis)

plt.figure(figsize=(6,4))
sns.countplot(x='City', data=df)
plt.title("Count of Houses by City")
plt.xlabel("City")
plt.ylabel("Number of Houses")
plt.xticks(rotation=45)
plt.show()

