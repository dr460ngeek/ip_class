import pandas as pd #importing pandas
import numpy as np #importing numpy

s=pd.Series([34,56,78,21,90])
print(s[1:])
print(s[2:5])
print(s[0::2])
s[0:4]=[23,32,87,19]
print(s)