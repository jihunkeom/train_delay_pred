import pandas as pd
import numpy as np
import random as rd

AD=[]

a = pd.read_csv('test.csv').drop(['Unnamed: 0'], axis=1)

b = a.values[0]

def threeSet(AD,b):
    cnt = 0;
    for i in range(6,59):
        if b[i]==0:
            b[i] = None
            cnt += 1
    n = int((len(b)-6-cnt)/5)
    rnd = []
    for i in range(n):
        i = rd.randint(6,58)
        b[i] = None
    notnull=[]
    for i in range(6,59):
        if pd.notnull(b[i]):
            notnull.append(i)
    if len(notnull)<=2:
        return AD
    for i in range(len(notnull)-2):
        if b[5]==0:
            AD.append(list(b[:6]) + [notnull[i] - 6, notnull[i + 1] - 6, notnull[i + 2] - 6,b[notnull[i]], b[notnull[i + 1]],b[notnull[i + 2]]])
        else:
            AD.append(list(b[:6]) + [58 - notnull[i + 2],58 - notnull[i + 1], 58 - notnull[i],b[notnull[i + 2]] ,b[notnull[i + 1]], b[notnull[i]]])
    return AD

def fillThreeSet(AD,df):
    for item in df.values:
        AD = threeSet(AD,item)
    return AD

# result=fillThreeSet(AD,a)
# result = pd.DataFrame(result)
# print(result[:150])
# result.to_csv('test3set.csv',index=False)