# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:18:44 2019

@author: H.J. Jia
"""

import json

with open('newfile2.json', 'r') as f:
    data = json.load(f)
    
new_dict = dict()

for i in data:
    key = list(i.keys())[0]
    value = list(i.values())[0]
    new_dict[key] = value

import pandas as pd
courses = pd.DataFrame.from_dict(new_dict,orient='index')
courses.to_csv('datacamp_courses.csv')