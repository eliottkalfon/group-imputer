# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 08:40:18 2020

@author: eliott.kalfon
"""

import pandas as pd
import numpy as np


data_dict = {'column1':[1,1,1,1,2,2,2,2,3,3,3,3],
        'column2':[2,3,2,np.nan,6,7,8,np.nan,np.nan,np.nan,np.nan,np.nan],
        'column3':[12,11,12,np.nan,17,23,18,np.nan,np.nan,np.nan,np.nan,np.nan]}

df = pd.DataFrame(data_dict)
#df = df[df['column1']<3]
print(df)

gb = df.groupby('column1')

func = lambda grp: grp.sum()
print(gb.apply(func))

for grp in gb