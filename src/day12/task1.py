# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:06:37 2026

@author: yashwith de
"""
import matplotlib.pyplot as plt


study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]


plt.scatter(study_hours, scores)


plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")


plt.show()

