# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 17:08:46 2026

@author: yashwith de
"""

import matplotlib.pyplot as plt

categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")


months = [1, 2, 3, 4, 5]
trend_sales = [200, 250, 300, 280, 350]

plt.subplot(1, 2, 2)
plt.plot(months, trend_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.show()
