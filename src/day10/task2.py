# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 12:58:33 2026

@author: yashwith de
"""

import pandas as pd

df = pd.read_csv("task2_price_dataset.csv")

print("Before conversion:\n")
print(df.dtypes)


df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)


df["Date"] = pd.to_datetime(df["Date"])

print("\nAfter conversion:\n")
print(df.dtypes)

