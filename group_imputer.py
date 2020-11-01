# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 07:37:05 2020

@author: eliott.kalfon

To do
- Accept np array as input
- Deal with null column average
- Use column indices and column names - check data types
- Input as numpy array 
- Different imputation strategies
- Dual/multiplr group by
- Custom imputation function with lambda expressions (start with mean and average)
- list or single value for imputed columns (start with list)
"""

import pandas as pd
import numpy as np


data_dict = {'column1':[1,1,1,1,2,2,2,2,3,3,3,3],
        'column2':[2,3,2,np.nan,6,7,8,np.nan,np.nan,np.nan,np.nan,np.nan],
        'column3':[12,11,12,np.nan,17,23,18,np.nan,np.nan,np.nan,np.nan,np.nan]}

df = pd.DataFrame(data_dict)
print(df)

class GroupImputer():
    '''
    Class to be used as group null imputer - work in progress.
    The objective is to take a dataframe or array as input, and returning the
    same object, with null values imputed based on within group average/median
    (or custom function, to be applied to the array)
    '''
    def __init__(self, strategy = 'mean'):
        self.col_means = {}
        self.group_means = {}
        self.strategy = strategy
        self.groupby_column = None
        self.group_values = None
        self.imputed_columns = None
        
    def fit(self, data, groupby_column, imputed_columns):
        # Updating the groupy and imputed column attributes
        self.groupby_column = groupby_column
        self.imputed_columns = imputed_columns
        # Getting the unique group values
        self.group_values = data[groupby_column].unique()
        # Creating a list of selected columns, composed of imputed and groupby columns
        selected_columns = self.imputed_columns + [self.groupby_column]
        # Getting a dictionary of means by column/group
        self.group_means = df[selected_columns].groupby(by=self.groupby_column).mean().to_dict()
        # Getting a dictionary of means by column (used for imputation when a group is filled with NAs)
        self.col_means = df[self.imputed_columns].mean().to_dict()
        
    def impute_column(self, column_name, data):
        # Iteration over groups
        for group in self.group_values:
            # Imputation value selection
            # If the group mean is null, then use the column mean
            if self.group_means[column_name][group] == self.group_means[column_name][group]:
                imputation_value = self.group_means[column_name][group]
            else:
                imputation_value = self.col_means[column_name]
            # Filtering the data with pandas loc operator
            data.loc[
                # Filtering to a single group
                (data[self.groupby_column]==group) & 
                # Filtering to null values
                (data[column_name]!=data[column_name]),
                # Selecting the column
                column_name
            # Imputing the selection with the imputation value
            ] = imputation_value
        return data
    
    def transform(self, data):
        if isinstance(self.imputed_columns, str):
            data = self.impute_column(column_name = self.imputed_columns, data = data)
        else:
            # Iteration over columns to impute
            for imputed_column in self.imputed_columns:
                data = self.impute_column(column_name = imputed_column, data = data)
        return data
    
    def fit_transform(self,data,groupby_column,imputed_columns):
        self.fit(data,groupby_column,imputed_columns)
        self.transform(data)

gi = GroupImputer()
# gi.fit(df, 'column1', ['column2', 'column3'])
# gi.transform(df)
gi.fit_transform(df,'column1', ['column2', 'column3'])
print(df)