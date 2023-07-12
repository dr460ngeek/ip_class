import pandas as pd

s = pd.Series([11,22,33,44,55],index=['a', 'b', 'c', 'd', 'e'])
'''
print("-------------------------")
print (s[:1])# for 1 index position
print("-------------------------")
print (s[:3]) #for first 3 index values
print("-------------------------")
print (s[1:])# slicing after 0 index position
print("-------------------------")
print (s[3:]) # slicing after 3 index values
print("-------------------------")
print (s[-3:]) # slicing for last 3 index values
'''
print(s[['b','a']])