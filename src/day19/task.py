# -*- coding: utf-8 -*-
"""
Created on Tue Feb 24 11:16:26 2026

@author: yashwith de
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

plt.figure()
plt.bar(x, y)
plt.title("Bar Chart")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.figure()
plt.hist(data)
plt.title("Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()