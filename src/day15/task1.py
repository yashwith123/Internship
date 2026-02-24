# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 10:14:14 2026

@author: yashwith de
"""

import random

# Number of simulations
trials = 1000
count_sum_7 = 0


for _ in range(trials):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    if die1 + die2 == 7:
        count_sum_7 += 1

experimental_probability = count_sum_7 / trials

print("Number of times sum was 7:",count_sum_7)
print("Experimental Probability of sum = 7:", experimental_probability)