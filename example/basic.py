# -*- coding: utf-8 -*-
"""

@author: eliott.kalfon

"""

import pandas as pd
import numpy as np
# Importing package
from group_imputer.group_imputer import  GroupImputer

# Generating sample dataframe
data_dict = {'group':[1,1,1,1,2,2,2,2,3,3,3,3],
        'column1':[2,3,2,np.nan,6,7,8,np.nan,np.nan,np.nan,np.nan,np.nan],
        'column2':[12,11,12,np.nan,17,23,18,np.nan,np.nan,np.nan,np.nan,np.nan]}

df = pd.DataFrame(data_dict)

print('Before imputation')
print(df)
print('\n')

# Creating a GroupImputer object
gi = GroupImputer(strategy = 'median')
# Imputing values in column 1 and 2, using the "group" column
gi.fit_transform(df,'group', ['column1', 'column2'])
# Displaying results
print('After imputation')
print(df)