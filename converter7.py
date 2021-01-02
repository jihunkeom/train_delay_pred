import pandas as pd
import numpy as np

AD=[]

a = pd.read_csv('trainv2.csv')

b = a.values[0]

def threeSet(AD,b):
    notnull=[]
    for i in range(6,59):
        if pd.notnull(b[i]):
            notnull.append(i)
    if len(notnull)<=2:
        return AD
    for i in range(len(notnull)-2):
        dat = []
        if b[5]==0:
            dat = list(b[:6]) + [notnull[i] - 6, notnull[i + 1] - 6, notnull[i + 2] - 6,b[notnull[i]], b[notnull[i + 1]],b[notnull[i + 2]]]
            AD.append(dat)
            dat = list(b[:6]) + [notnull[i + 1] - 6,notnull[i] - 6, notnull[i + 2] - 6, b[notnull[i + 1]],b[notnull[i]],b[notnull[i + 2]]]
            AD.append(dat)
            dat = list(b[:6]) + [notnull[i] - 6, notnull[i + 2] - 6,notnull[i + 1] - 6,b[notnull[i]],b[notnull[i + 2]],b[notnull[i + 1]]]
            AD.append(dat)
        else:
            dat = list(b[:6]) + [58 - notnull[i + 2],58 - notnull[i + 1], 58 - notnull[i],b[notnull[i + 2]] ,b[notnull[i + 1]], b[notnull[i]]]
            AD.append(dat)
            dat = list(b[:6]) + [ 58 - notnull[i + 1],58 - notnull[i + 2], 58 - notnull[i],
                                 b[notnull[i + 1]],b[notnull[i + 2]], b[notnull[i]]]
            AD.append(dat)
            dat = list(b[:6]) + [58 - notnull[i + 2], 58 - notnull[i],58 - notnull[i + 1], b[notnull[i + 2]],
                                  b[notnull[i]],b[notnull[i + 1]]]
            AD.append(dat)
    return AD

def fillThreeSet(AD,df):
    for item in df.values:
        AD = threeSet(AD,item)
    return AD

# result=fillThreeSet(AD,a)
# result = pd.DataFrame(result)
# print(result[:150])
# result.to_csv('train3setV2.csv',index=False)