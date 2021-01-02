import pandas as pd
from datetime import datetime, timedelta
import requests

############################################### FUNCTION ###############################################################

def getTrainList(df):
    trainList = df['열차번호'].values
    return trainList

def getStationList(df):
    stationList = df.columns[3:].values
    return stationList

def getList(train,date):
    URL = "https://rail.blue/railroad/logis/getmagiainfo.aspx?train={}&date={}".format(train, date)
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Host': 'rail.blue',
    }
    res = requests.post(URL, headers=headers)
    print('load end')
    arr = res.text.split('\n')[2:]
    list = {'station': [], 'delay': []}
    for elem in arr:
       lst = elem.split('|')
       if (lst[0] != ''):
          list['station'].append(lst[0])
          if (len(lst) < 5):
              list['delay'].append(10000)#data가 없는 경우 10000을 할당
          else:
              if(lst[4]!=''):
                  list['delay'].append(lst[4])
              else:
                  list['delay'].append(10000)
    return list

def setDelay(df,list,train):
    j = 0
    stationList = getStationList(df)
    for station in stationList:
        if(station[:2] == list['station'][j][:2]):
            df.at[train,station] = list['delay'][j]
            j += 1
        if(len(list['station'])-1<j):
            break
    return df

def fillSheet(timeTable,sheet_name,date):
    df = timeTable.parse(sheet_name)
    trainList = getTrainList(df)
    for i in range(len(trainList)):
        print(trainList[i])
        list = getList(trainList[i],date)
        df = setDelay(df,list,i)
    return df, sheet_name

def crowlDate(dateform,timeTable,sheet_list,holiday):
    print(dateform.date())
    print('holiday: '+str(holiday))
    if holiday or dateform.weekday() == 6:
        sheet_list = sheet_list['일']
    elif dateform.weekday() < 5:
        sheet_list = sheet_list['평']
    else:
        sheet_list = sheet_list['토']
    with pd.ExcelWriter(str(dateform.date()) + '.xls') as writer:
        for item in sheet_list:
            df, sheet_name = fillSheet(timeTable,item,str(dateform.date())[:4]+str(dateform.date())[5:7]+str(dateform.date())[8:10])
            df.to_excel(writer,sheet_name = item,index=False)

def crowlTrainDelay(start_date,crowl_days,holidays):
    path = ["200601time.xlsx", "200302time.xlsx", "190801time.xlsx"] #기준이 되는 시간표 경로
    # sheet_list = {'평':["평일상 경의중앙선","평일하 경의중앙선"],'토':["토상행 경의중앙선","토하행 경의중앙선"],'일':["일상행 경의중앙선","일하행 경의중앙선"]}
    sheet_list = {'평': ["평일상 경의중앙선", "평일하 경의중앙선"], '토': ["토일공휴상 경의중앙선", "토일공휴하 경의중앙선"],
                  '일': ["토일공휴상 경의중앙선", "토일공휴하 경의중앙선"]}
    for i in range(crowl_days):
        date = start_date-timedelta(days=i)
        holiday = 0
        if date in holidays:
           holiday = 1
        if date > datetime(2020,6,1):
            timeTable = pd.ExcelFile(path[0])
        elif date > datetime(2020,3,2):
            timeTable = pd.ExcelFile(path[1])
        else:
            timeTable = pd.ExcelFile(path[2])
        crowlDate(date,timeTable,sheet_list,holiday)

    return print("Success!")


########################################################################################################################
################################################## CONTROL #############################################################

start_date = datetime(2020,1,11) #기준일, 연 월 일 순
crowl_days = 11  # 기준 시작일부터 거꾸로 긁어옴 10일 -> 9일 -> 8일 ...
holidays = [datetime(2020,10,9),datetime(2020,10,3),datetime(2020,10,2),datetime(2020,10,1),datetime(2020,9,30),datetime(2020,8,17),datetime(2020,4,15),datetime(2020,5,5),datetime(2020,4,30),datetime(2020,3,1),datetime(2020,1,27),datetime(2020,1,26),datetime(2020,1,25),datetime(2020,1,24),datetime(2020,1,1)] # 긁어올 날 안에 일요일 토요일 제외 공휴일이 있다면 표시해줘야함


crowlTrainDelay(start_date,crowl_days,holidays)

## 결과 해석 : 일자, 열차번호, 역 별로 지연시간(+ or -)을 초단위로 기록, 결측치는 일괄 '10000'으로 할당