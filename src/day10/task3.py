# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 19:43:43 2026

@author: yashwith de
"""

import pandas as pd


df = pd.read_csv("task3_location_dataset.csv")

print("Before cleaning:")
print(df["Location"].unique())


df["Location"] = df["Location"].str.strip()


df["Location"] = df["Location"].str.title()

print("\nAfter cleaning:")
print(df["Location"].unique())
