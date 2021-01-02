import pandas as pd
from datetime import datetime, timedelta
import numpy as np

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
        if a[j] == 10000.0:
            a[j] = np.nan
        # elif a[j]!=0:
        #     k += 1
    AD_frac = AD_frac + list(a)
    if k >0:
        AD.append(AD_frac)
    return AD, df

def fillUp(AD,df,updown,holiday,weekday):
    for i in range(len(df.values)):
        setup(AD,df,i,updown,holiday,weekday)
    return AD, df

def fillDayUp(data,AD,holiday,weekday):
    updown = 0
    for sheet in data.sheet_names:
        print(sheet)
        df = data.parse(sheet)
        AD,_ = fillUp(AD,df,updown,holiday,weekday)
        updown = 1
    return AD

def fillAuto(AD,start_date,fill_date,holidays):
    for i in range(fill_date):
        date = start_date-timedelta(days=i)
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

AD = fillAuto(AD, start_date, fill_date, holidays)
result = pd.DataFrame(AD)
result.to_csv('train_ext.csv',index=False)




