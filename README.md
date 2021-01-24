![](https://github.com/eliottkalfon/group-imputer/blob/main/resources/logo.png)

# Description
Null imputation utility filling null values with group specific aggregates (mean, median, min, custom value etc...). It is particularly useful in datasets with high cross-categorical variance, in which null imputation by null values would generate information loss.
<br>It uses pandas dataframes in the back-end

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


# Credits

- Icon featured in the logo: Icon made by <div>Icons made by <a href="https://www.flaticon.com/authors/pixel-perfect" title="Pixel perfect">Pixel perfect</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>