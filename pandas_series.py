import pandas as pd
s1=pd.Series([1,2,3,4,5])
s1



# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

s1=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
s1
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64

pd.Series({'a':10,'b':20,'c':30}, index=['b','c','d'])
# b    20.0
# c    30.0
# d     NaN
# dtype: float64
