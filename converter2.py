import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import data_helper as dh



def setup(AD,df,i,ud,holiday,weekday):
    if ud == 'up':
        updown=0
        if np.isnan(df.values[i][(dh.getStationNum(df.values[i][0]) + 4)])or np.isnan(
                df.values[i][(dh.getStationNum(df.values[i][1]) + 2)]):
            return
    else:
        updown=1
        if np.isnan(df.values[i][(53-dh.getStationNum(df.values[i][0]) + 4)])or np.isnan(
                df.values[i][(53-dh.getStationNum(df.values[i][1]) + 2)]):
            return
    AD_frac = []
    AD_frac.append(df.values[i][2])
    AD_frac.append(weekday)
    AD_frac.append(holiday)
    AD_frac.append(df.values[i][0])
    AD_frac.append(df.values[i][1])
    AD_frac.append(updown)
    a = list(df.values[i][3:])
    for l in range(len(a)):
        if np.isnan(a[l]):
            a[l]=0
        break
    for l in range(len(a)-1,-1,-1):
        if np.isnan(a[l]):
            a[l]=0
        break
    if updown == 1:
        a.reverse()
    k = 1
    for j in range(len(a)):
        if pd.isna(a[j]):
            a[j]=0
        if a[j] == 10000.0:
            a[j] = np.nan
        # elif a[j]!=0:
        #     k += 1
    ts = pd.Series(a)
    ts = ts.interpolate(method="values")
    ts.fillna(method='ffill')
    AD_frac = AD_frac + list(ts.values)
    if k >0:
        AD.append(AD_frac)
    return AD

def fillUp(AD,df,updown,holiday,weekday):
    for i in range(len(df.values)):
        setup(AD,df,i,updown,holiday,weekday)
    return AD


def fillAuto(AD,start_date,fill_date,holidays):
    for i in range(fill_date):
        date = start_date-timedelta(days=i)
        holiday = 0
        if date in holidays:
            holiday = 1
        for ud in ['up','down']:
            data = pd.read_csv(str(date.date()) + '-{}-delay.csv'.format(ud),encoding="cp949")
            fillUp(AD, data, ud, holiday, date.weekday())
    return AD

start_date = datetime(2020,11,17)
fill_date = 7
holidays = [datetime(2020,10,9),datetime(2020,10,3),datetime(2020,10,2),datetime(2020,10,1),datetime(2020,9,30),datetime(2020,8,17),datetime(2020,4,15),datetime(2020,5,5),datetime(2020,4,30)] # 긁어올 날 안에 일요일 토요일 제외 공휴일이 있다면 표시해줘야함

AD = []

AD = fillAuto(AD,start_date,fill_date,holidays)
result = pd.DataFrame(AD)
result.to_csv('test.csv',encoding='utf-8')

# def setup(AD,df,i,updown,holiday,weekday):
#     AD_frac = []
#     AD_frac.append(df.values[i][2])
#     AD_frac.append(weekday)
#     AD_frac.append(holiday)
#     AD_frac.append(df.values[i][0])
#     AD_frac.append(df.values[i][1])
#     AD_frac.append(updown)
#     a = list(df.values[i][3:])
#     if updown == 1:
#         a.reverse()
#     if a[0]==10000:
#         a[0] = 0
#     # if a[len(a)-1]==10000:
#     #     a[len(a) - 1]== 0
#     k = 1
#     for j in range(len(a)):
#         if pd.isna(a[j]):
#             a[j]=0
#         if a[j] == 10000.0:
#             a[j] = np.nan
#         # elif a[j]!=0:
#         #     k += 1
#     ts = pd.Series(a)
#     ts = ts.interpolate(method="values")
#     ts.fillna(method='ffill')
#     AD_frac = AD_frac + list(ts.values)
#     if k >0:
#         AD.append(AD_frac)
#     return AD
#
# def fillUp(AD,df,updown,holiday,weekday):
#     for i in range(len(df.values)):
#         setup(AD,df,i,updown,holiday,weekday)
#     return AD
#
#
# def fillAuto(AD,start_date,fill_date,holidays):
#     for i in range(fill_date):
#         date = start_date-timedelta(days=i)
#         holiday = 0
#         if date in holidays:
#             holiday = 1
#         for ud in ['up','down']:
#             data = pd.read_csv(str(date.date()) + '-{}-delay.csv'.format([ud]))
#             AD = fillUp(AD,data,ud,holiday,date.weekday())
#     return AD
#
# start_date = datetime(2020,9,29)
# fill_date = 212
# holidays = [datetime(2020,9,20),datetime(2020,9,21),datetime(2020,9,22),datetime(2020,8,17),datetime(2020,6,6),datetime(2020,4,15),datetime(2020,5,5),datetime(2020,4,30)]
#
# AD = []
#
# AD = fillAuto(AD,start_date,fill_date,holidays)
# result = pd.DataFrame(AD)
# result.to_csv('train.csv')