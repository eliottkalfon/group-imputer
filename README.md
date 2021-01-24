![](https://github.com/eliottkalfon/group-imputer/blob/main/resources/logo.png)

# Description
Null imputation utility filling null values with group specific aggregates (mean, median, min, custom value etc...). It is particularly useful in datasets with high cross-categorical variance, in which null imputation by dataset aggregations would generate information loss.
<br>It uses pandas dataframes in the back-end, and has the fit(), transform(), and fit_transform() methods - important to avoid information leak across the train/test separation.

# Installation

This package can be installed with "pip" or by cloning this repository

    $ pip install group-imputer
	
# Dependencies

To install and run group-imputer make sure that you have installed the following packages

    $ pip install numpy pandas
	
# Importing group-imputer

```python
import numpy as np
import pandas as pd
from group_imputer.group_imputer import GroupImputer
```

# Using the group-imputer

A basic example usage can be found in the [example folder](https://github.com/eliottkalfon/group-imputer/tree/main/example).

```python
# Creating a GroupImputer object
gi = GroupImputer(strategy = 'median')
# Imputing values in column 1 and 2, using the "group" column
gi.fit_transform(df,'group', ['column1', 'column2'])
```

# Credits

- Icon featured in the logo: Icon made by <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>