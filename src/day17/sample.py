# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 12:01:54 2026

@author: yashwith de
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\sqlite\sample.db")
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)