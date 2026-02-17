# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 14:13:16 2026

@author: yashwith de
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("housing_data.csv")
plt.subplot(1,2,1)
sns.scatterplot(x=df["Area_sqft"], y=df["Price"])
plt.title("House Size vs Price")
plt.xlabel("Area (sqft)")
plt.ylabel("Price")
plt.tight_layout()
plt.subplot(1,2,2)
sns.boxplot(x=df["City"], y=df["Price"])
plt.title("City vs Price Distribution")
plt.xlabel("City")
plt.ylabel("Price")
plt.show()