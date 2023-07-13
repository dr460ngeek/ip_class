import pandas as pd1
data1 = {'Name':['Freya', 'Mohak'],'Age':[9,10]}
df1 = pd1.DataFrame(data1)
df1 = pd1.DataFrame(data1, index=['rank1','rank2'])
print (df1)