# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:36:46 2026

@author: yashwith de
"""

import pandas as pd


grades = pd.Series([85, None, 92, 45, None, 78, 55])
missing = grades.isnull()
filled_grades = grades.fillna(0)
filtered = filled_grades[filled_grades > 60]


print("Original Series:")
print(grades)

print("\nMissing values :")
print(missing)

print("\nSeries after filling values with 0:")
print(filled_grades)

print("\nScores greater than 60:")
print(filtered)
