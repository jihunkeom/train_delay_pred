# 라이브러리 import
import sys
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import base64

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
path = "200302_Monsan-YongMun.xls"
rail = "Korail"

timeTable = pd.ExcelFile(path)
SP = [2,4]
stationSP = [2,4]
trainSP = [3,2]

station = 1

def station2b64(timeTable,station,SP,sheet_name):
    stationName = timeTable.parse(sheet_name=sheet_name)['Unnamed: '+str(station+SP[1])].values[SP[0]-1]
    if(stationName[0] == '1'):
        stationName = stationName[1:]
    print(stationName)
    return base64.urlsafe_b64encode(stationName.encode('utf-8')).decode('utf-8')

def getTrainLate(timeTable,station,SP,list,sheet_name):
    parsed = timeTable.parse(sheet_name=sheet_name)
    trainList = parsed['Unnamed: '+str(station+SP[1])].values[SP[0]:]
    trainName = parsed['Unnamed: '+str(SP[1]-2)].values[SP[0]:]
    for i in range(len(trainList)):
        if not pd.isnull(trainList[i]):
            for j in range(len(list['train'])):
                if trainName[i]== list['train'][j]:
                    trainList[i] = list['delay'][j]
    return trainList, ['Unnamed: '+str(station+SP[1]),SP[0]]

def setTrainLate(df, trainLate, location):
    df.at[location[1]:,location[0]] = trainLate
    return df

# 파이어폭스를 사용해 오글 로리 사이트 접속.
# 이유: 오글 로리는 Javascript를 사용해 동적으로 전철운행정보를 불러오기 때문.
def getList(b64name,date,driver):
    driver.get('https://rail.blue/railroad/logis/metrodriveinfo.aspx?q={}&c={}&date={}&hr=0&min=0&base=1&qv=#!'.format(b64name,rail,date))


    #0.5초마다 스크롤 25번 내리는 효과로 전체 시간표를 불러옴.
    if b64name == '7Jqp7IKw':
        for i in range(35):
            print(i)
            driver.execute_script('ScrollLoad();')
            time.sleep(0.5)
    else:
        for i in range(25):
            print(i)
            driver.execute_script('ScrollLoad();')
            time.sleep(0.5)

    # BeautifulSoup 4를 사용해 HTML 코드 크롤링
    html = driver.page_source
    soup = BeautifulSoup(html, features="lxml")

    # train_list: 열차번호 및 지연 정보 등 정차 리스트
    # updown_list: 상하행 정보
    train_list = soup.find_all("tr", {"id": re.compile(r'trtn_*')})
    notpass_list = soup.find_all("td", {"class": "tdResult_UpDown"})
    # 인덱스를 맞춰주기 위해 타이틀 관련 앞의 2개 제외하고,
    # updown에 상행/하행이 아닌 관련 없는 정차(중간중간에 끼어 있음)/통과가 있으면 리스트에서 제외.
    notpass_list = notpass_list[2:]
    notpass_list = [item for item in notpass_list if '정차' not in item.text and '통과' not in item.text]
    # 본격적인 크롤링 및 상행과 하행을 분류
    list = {'train': [], 'delay': []}
    for i, tr in enumerate(train_list):
        td = tr.find_all("td")
        # td에는 열차번호(1)와 지연시간(4)이 있다.
        if '통과' not in notpass_list[i].text:  # 상행일 경우
            list['train'].append(td[1].text.strip())
            list['delay'].append(td[4].text.strip())
    return list
# 파일로 저장
# 형식: 날짜_up.csv, 날짜_down.csv
# df = pd.DataFrame(list)
# df.to_csv(date + '.csv')
date = "20201008"

sheet_name = "평일상 경의중앙선"
driver = webdriver.Firefox()
df_up = timeTable.parse(sheet_name=sheet_name)
for i in range(53):
    station = i
    station_b64 = station2b64(timeTable,station,SP,sheet_name)
    list = getList(station_b64,date,driver)
    a,b = getTrainLate(timeTable,station,SP,list,sheet_name)
    df_up = setTrainLate(df_up,a,b)

sheet_name = "평일하 경의중앙선"
driver = webdriver.Firefox()
df_down = timeTable.parse(sheet_name=sheet_name)
for i in range(53):
    station = i
    station_b64 = station2b64(timeTable,station,SP,sheet_name)
    list = getList(station_b64,date,driver)
    a,b = getTrainLate(timeTable,station,SP,list,sheet_name)
    df_down = setTrainLate(df_down,a,b)


writer = pd.ExcelWriter(date+'.xls')
df_up.to_excel(writer,sheet_name = sheet_name,index=False)
writer.close()
#result = pd.DataFrame(timeTable)
#result.to_excel(date+'.xls')

# # trainNum = trainNum[pd.notnull(trainNum)][1:]
# trainNum = timeTable.parse(sheet_name="평일상 경의중앙선")
# station = trainNum[1:2].values[0]
# print(station[0][1])

# def getStationList(timeTable,sheet_name):
#     stationList = timeTable.parse(sheet_name=sheet_name)
#     stationList = stationList[1:2].values[0][4:]
#     for i in range(len(stationList)):
#         if(stationList[i][0] == '1'):
#             stationList[i] = stationList[i][1:]
#     return stationList
#
# def getTrainList(timeTable,sheet_name,station):
#     trainList = timeTable.parse(sheet_name=sheet_name)['Unnamed: 2'].values
#     print(trainList)
#  #   trainList = trainList[pd.notnull(trainList)][2:].values
#     return trainList
#
# def location(ifstation,i):
#     if ifstation == 1:
#         return [2,4+i]
#     else:
#         return [3+i,2]


# stationList = getStationList(timeTable,"평일상 경의중앙선")
# station = stationList[0]
# trainList = getTrainList(timeTable,"평일상 경의중앙선",station)
# print(trainList)



# # 파이어폭스를 사용해 오글 로리 사이트 접속.
# # 이유: 오글 로리는 Javascript를 사용해 동적으로 전철운행정보를 불러오기 때문.
# driver = webdriver.Firefox()
# station_b64 = base64.urlsafe_b64encode(station.encode('utf-8')).decode('utf-8')
# driver.get('https://rail.blue/railroad/logis/metrodriveinfo.aspx?q={}&c={}&date={}&hr=0&min=0&base=1&qv=#!'.format(station_b64,rail,date))
#
#
# #0.5초마다 스크롤 20번 내리는 효과로 전체 시간표를 불러옴.
# for i in range(20):
#     print(i)
#     driver.execute_script('ScrollLoad();')
#     time.sleep(0.5)
#
# # BeautifulSoup 4를 사용해 HTML 코드 크롤링
# html = driver.page_source
# soup = BeautifulSoup(html, features="lxml")
#
#
# # train_list: 열차번호 및 지연 정보 등 정차 리스트
# # updown_list: 상하행 정보
# train_list = soup.find_all("tr", {"id": re.compile(r'trtn_*')})
# updown_list = soup.find_all("td", {"class": "tdResult_UpDown"})
# # 인덱스를 맞춰주기 위해 타이틀 관련 앞의 2개 제외하고,
# # updown에 상행/하행이 아닌 관련 없는 정차(중간중간에 끼어 있음)/통과가 있으면 리스트에서 제외.
# updown_list = updown_list[2:]
# updown_list = [
#     item for item in updown_list if '정차' not in item.text and '통과' not in item.text]
#
# # 본격적인 크롤링 및 상행과 하행을 분류
# up_list = {'train': [], 'delay': []}
# down_list = {'train': [], 'delay': []}
#
# for i, tr in enumerate(train_list):
#     td = tr.find_all("td")
#     if '정차' in td[0].text:  # td(0)에 정차가 표시된 경우
#         # td에는 열차번호(1)와 지연시간(4)이 있다.
#         if '상행' in updown_list[i].text:  # 상행일 경우
#             up_list['train'].append(td[1].text.strip())
#             up_list['delay'].append(td[4].text.strip())
#
#         if '하행' in updown_list[i].text:  # 하행일 경우
#             down_list['train'].append(td[1].text.strip())
#             down_list['delay'].append(td[4].text.strip())
#
# # 파일로 저장
# # 형식: 날짜_up.csv, 날짜_down.csv
# up_df = pd.DataFrame(up_list)
# down_df = pd.DataFrame(down_list)
# up_df.to_csv(date + '_up.csv',)
# down_df.to_csv(date + '_down.csv')