import pandas as pd
import numpy as np
import random as rd

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
        if b[5]==0:
            AD.append(list(b[:6]) + [notnull[i] - 6, notnull[i + 1] - 6, notnull[i + 2] - 6,b[notnull[i]], b[notnull[i + 1]],b[notnull[i + 2]]])
            rand = rd.sample(notnull,3)
            rand.sort()
            AD.append(list(b[:6]) + [rand[0] - 6, rand[1] - 6, rand[2] - 6,b[rand[0]], b[rand[1]],b[rand[2]]])
        else:
            AD.append(list(b[:6]) + [58 - notnull[i ],58 - notnull[i + 1], 58 - notnull[i+2],b[notnull[i ]] ,b[notnull[i + 1]], b[notnull[i+2]]])
            rand = rd.sample(notnull,3)
            rand.sort()
            AD.append(list(b[:6]) + [58 - rand[0], 58 - rand[1], 58 - rand[2], b[rand[0]],
                                     b[rand[1]], b[rand[2]]])
    return AD

def fillThreeSet(AD,df):
    for item in df.values:
        AD = threeSet(AD,item)
    return AD

# result=fillThreeSet(AD,a)
# result = pd.DataFrame(result)
# print(result[:150])
# result.to_csv('train3setOrderRand.csv',index=False)