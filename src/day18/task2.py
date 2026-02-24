# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 12:09:35 2026

@author: yashwith de
"""

import sqlite3
import pandas as pd

# Connect to correct database
conn = sqlite3.connect(r"C:\sqlite\internship1.db")

query = """
SELECT interns.name,
       interns.track,
       mentors.mentor_name,
       interns.stipend
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track;
"""

df = pd.read_sql_query(query, conn)

df