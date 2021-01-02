import pandas as pd
import numpy as np

AD=[]

a = pd.read_csv('trainv2.csv')

b = a.values[0]

def twoSet(AD,b):
    notnull=[]
    for i in range(6,59):
        if pd.notnull(b[i]):
            notnull.append(i)
    for i in range(len(notnull)):
        if b[5]==0:
            AD.append(list(b[:6])+[notnull[i]-5,b[notnull[i]]])
        else:
            AD.append(list(b[:6])+[58-notnull[i],b[notnull[i]]])
    return AD

def fillTwoSet(AD,df):
    for item in df.values:
        AD = twoSet(AD,item)
    return AD

result=fillTwoSet(AD,a)
result = pd.DataFrame(result)
print(result[:150])
#result.to_csv('train3.csv',index=False)