import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from datetime import datetime, timedelta



def getTrainList(df):
    trainList = df['Unnamed: 2'].values[pd.notnull(df['Unnamed: 2'].values)][1:]
    print(trainList)
    return trainList

def getList(train,date,driver):
    driver.get('https://rail.blue/railroad/logis/magiainfo.aspx?date={}&train={}#!'.format(date,train))
    #0.6초마다 스크롤 25번 내리는 효과로 전체 시간표를 불러옴.
    time.sleep(0.8)
    # for i in range(5):
    #     driver.execute_script('ScrollLoad();')
    #     time.sleep(0.5)
    print('scroll end')
    # BeautifulSoup 4를 사용해 HTML 코드 크롤링
    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")
    raw_list = soup.find_all("td", {"class": "tdResult_Line"})
    raw_list = [item for item in raw_list if '자동PI' not in item.text]
    list = {'station':[],'delay':[]}
    i = 0
    for td in enumerate(raw_list):
        if i%4 == 0:
            if(td[1].text.strip()=='디지털미디어시티'):
                list['station'].append('디엠시')
            else:
                list['station'].append(td[1].text.strip())
        elif i%4 == 3:
            if (td[1].text[0]=='+')or(td[1].text[0]=='-'):
                list['delay'].append(td[1].text.strip())
            else:
                list['delay'].append('no data')
        i += 1
    for j in range(len(list['station'])-1,-1,-1):
        if list['station'][j] == '':
            del list['delay'][j]
            del list['station'][j]
    return list

def setDelay(df,list,train):
    j = 0
    for i in range(53):
        if (pd.isna(df.iat[1,4 + i])):
            break
        if (df.iat[1,4 + i][0] == '1'):
            df.iat[1,4 + i] = df.iat[1,4 + i][1:]
        if(df.iat[1,4 + i][:2] == list['station'][j][:2]):
            df.iat[2+train,4+i] = list['delay'][j]
            j += 1
        elif pd.notnull(df.iat[2 + train, 4 + i]):
            df.iat[2 + train, 4 + i] = None
        if(len(list['station'])-1<j):
            break
    return df

def fillSheet(timeTable,sheet_name,date,driver):
    df = timeTable.parse(sheet_name)
    trainList = getTrainList(df)
    for i in range(len(trainList)):
        print(trainList[i])
        list = getList(trainList[i],date,driver)
        df = setDelay(df,list,i)
    return df, sheet_name

def crowlDate(dateform,timeTable,sheet_list,driver):
    print(dateform.date())
    if dateform.weekday() < 5:
        sheet_list = sheet_list['평']
    elif dateform.weekday() == 5:
        sheet_list = sheet_list['토']
    else:
        sheet_list = sheet_list['일']
    with pd.ExcelWriter(str(dateform.date()) + '.xls') as writer:
        for item in sheet_list:
            df, sheet_name = fillSheet(timeTable,item,date,driver)
            df.to_excel(writer,sheet_name = item,index=False)



path = "200302_Monsan-YongMun.xls"

timeTable = pd.ExcelFile(path)
sheet_list = {'평':["평일상 경의중앙선","평일하 경의중앙선"],'토':["토상행 경의중앙선","토하행 경의중앙선"],'일':["일상행 경의중앙선","일하행 경의중앙선"]}
start_date = datetime(2020,10,26)
crowl_days = 2
driver = webdriver.Firefox()



# list = getList('K5304',date,driver)
# df = setDelay(df,list,train)

for i in range(crowl_days):
    date = start_date-timedelta(days=i)
    crowlDate(date,timeTable,sheet_list,driver)


