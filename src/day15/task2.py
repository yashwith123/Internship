# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 10:29:21 2026

@author: yashwith de
"""

import random

trials = 100000
count_success = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])

    die = random.randint(1, 6)
    
    if coin == "H" and die == 6:
        count_success += 1

experimental_probability = count_success / trials

print("Independent Event:")
print("Experimental Probability:", experimental_probability)
print("Theoretical Probability:", 1/12)