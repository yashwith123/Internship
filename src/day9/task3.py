# -*- coding: utf-8 -*-
"""
Created on Wed Feb 11 12:49:50 2026

@author: yashwith de
"""
import pandas as pd


usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])


cleaned_usernames = usernames.str.strip().str.lower()


contains_a = cleaned_usernames.str.contains('a')


print("Cleaned Usernames:")
print(cleaned_usernames)

print("\nNames containing the letter 'a':")
print(contains_a)
