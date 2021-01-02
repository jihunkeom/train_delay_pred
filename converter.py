import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
from datetime import datetime, timedelta
from tensorflow.keras.models import load_model, Model
import numpy as np
from tensorflow.keras.layers import Dense, Dropout, Activation, Input
import tensorflow as tf
import data_helper as dh
import os
import pandas as pd

os.environ["KMP_DUPLICATE_LIB_OK"]='TRUE'

def inter(inform,piv1,piv2,val1,val2,want):
    #intput = [dh.oneHot('train', dh.getTrainNum(inform[0])) + dh.oneHot('weekdays', inform[1]) + [inform[2]]\
    #         + [inform[5]] + dh.oneHot('station', piv1) + dh.oneHot('station', want) + dh.oneHot('station', piv2) + [val1] + [val2]];
    #y_pred = model.predict(np.array(intput))
    return

def setup(AD,df,i,updown,holiday,weekday):

    AD_frac = []
    AD_frac.append(df.values[i][2])
    AD_frac.append(weekday)
    AD_frac.append(holiday)
    AD_frac.append(df.values[i][0])
    AD_frac.append(df.values[i][1])
    AD_frac.append(updown)
    a = list(df.values[i][3:])
    if updown == 1:
        a.reverse()
    if a[0]==10000:
        a[0] = 0
    # if a[len(a)-1]==10000:
    #     a[len(a) - 1]== 0
    k = 1
    for j in range(len(a)):
        if pd.isna(a[j]):
            a[j]=0
        if a[j] == 10000.0:
            a[j] = np.nan
        # elif a[j]!=0:
        #     k += 1
    notnulls=[]
    nulls=[]
    for i in range(len(a)):
        if pd.notnull(a[i]):
            notnulls.append(i)
        else:
            nulls.append(i)
    if len(notnulls)<8:
        return AD, df
    m=1
    global rc
    for i in range(len(nulls)):
        while (m<(len(notnulls)-1))&(nulls[i]>notnulls[m]):
            m+=1
        if updown ==0:
            a[nulls[i]] = res[rc][1]#inter(AD_frac,notnulls[m-1],notnulls[m],a[notnulls[m-1]],a[notnulls[m]],nulls[i])#a[nulls[i]] =
            rc += 1
        else:
            a[nulls[i]] = res[rc][1]#inter(AD_frac, notnulls[m], notnulls[m-1], a[notnulls[m]], a[notnulls[m-1]], nulls[i])#a[nulls[i]] =
            rc += 1
    AD_frac = AD_frac + a

    AD.append(AD_frac)
    return AD, df

def fillUp(AD,df,updown,holiday,weekday):
    for i in range(len(df.values)):
        setup(AD,df,i,updown,holiday,weekday)
    return AD, df

def fillDayUp(data,AD,holiday,weekday):
    updown = 0
    for sheet in data.sheet_names:
        df = data.parse(sheet)
        AD,_ = fillUp(AD,df,updown,holiday,weekday)
        updown = 1
    return AD

def fillAuto(AD,start_date,fill_date,holidays):
    for i in range(fill_date):
        date = start_date-timedelta(days=i)
        print(date)
        data = pd.ExcelFile(str(date.date()) + '.xls')
        holiday = 0
        if date in holidays:
            holiday = 1
        AD = fillDayUp(data,AD,holiday,date.weekday())
    return AD

start_date = datetime(2020,9,29)
fill_date = 273
holidays = [datetime(2020,10,9),datetime(2020,10,3),datetime(2020,10,2),datetime(2020,10,1),datetime(2020,9,30),datetime(2020,8,17),datetime(2020,4,15),datetime(2020,5,5),datetime(2020,4,30)] # 긁어올 날 안에 일요일 토요일 제외 공휴일이 있다면 표시해줘야함

AD = []
# xInput1 = Input(batch_shape=(None, 359))
# hidden1 = Dense(220, kernel_initializer='he_normal', activation=tf.nn.leaky_relu)(xInput1)
# hidden2 = Dense(110, kernel_initializer='he_normal', activation=tf.nn.leaky_relu)(hidden1)
# hidden3 = Dense(60, kernel_initializer='he_normal', activation=tf.nn.leaky_relu)(hidden2)
# output = Dense(1)(hidden3)
# model = Model(xInput1,output)
# model.load_weights('fcmodelw.h5')

res = pd.read_csv('res.csv')
res = res.values
print(res[1000][1])
global rc
rc = 0;
AD = fillAuto(AD,start_date,fill_date,holidays)
result = pd.DataFrame(AD)
result.to_csv('train_ext_filled.csv')
# kkk = pd.DataFrame(PD)
# kkk.to_csv('req.csv',index=False)



