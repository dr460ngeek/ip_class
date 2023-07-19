import pandas as pd

# Pandas Series
# Head & Tails function 
s = pd.Series([1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g'])
print("The orignal series is:\n", s) 
print("After using tail: \n", s.tail(3))
print("After using head: \n", s.head(3))