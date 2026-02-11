# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 14:32:30 2026

@author: yashwith de
"""
#concept 1
import pandas as pd

s1 = pd.Series([10, 20, 30, 40])
s2 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

print(s1)
print(s2)

#concept 2
marks = pd.Series([85, 90, 78], index=['Math', 'Physics', 'Chemistry'])

print(marks['Math'])
print(marks[['Math', 'Chemistry']])

#topic 3
scores = pd.Series([45, 67, 89, 34, 90])

passed = scores[scores > 60]
print(passed)

#topic 4
data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(3))

#topic 5
names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('o'))
