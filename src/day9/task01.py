# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:30:14 2026

@author: yashwith de
"""

import pandas  as pd
products = pd.Series([850, 170, 320], index=['Laptop', 'Mouse', 'Keyboard'])

laptop_price = products['Laptop']
first_two =products[:2]

print("Full Series:")
print(products)
print("\nPrice of Laptop:")
print(laptop_price)
print("\nFirst two products slicing:")
print(first_two)