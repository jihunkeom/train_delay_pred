import pandas as pd
import numpy as np
from datetime import datetime, timedelta, time


station_list = ['지평', '용문', '원덕', '양평', '오빈', '아신', '국수', '신원',
       '양수', '운길산', '팔당', '도심', '덕소', '1양정', '도농', '구리', '1양원', '망우', '상봉',
       '중랑', '회기', '청량리', '왕십리', '응봉', '옥수', '한남', '서빙고', '이촌', '용산', '효창공',
       '공덕', '서강대', '홍대입', '가좌', '디엠시', '수색', '화전', '강매', '행신', '능곡', '대곡',
       '곡산', '백마', '풍산', '일산', '탄현', '야당', '운정', '금릉', '금촌', '월롱', '파주', '문산']
station_list_n = ['지평', '용문', '원덕', '양평', '오빈', '아신', '국수', '신원',
       '양수', '운길산', '팔당', '도심', '덕소', '1양정', '도농', '구리', '1양원', '망우', '상봉',
       '중랑', '회기', '청량리', '왕십리', '응봉', '옥수', '한남', '서빙고', '이촌', '용산', '효창공원앞',
       '공덕', '서강대', '홍대입구', '가좌', '디지털시티', '수색', '화전', '강매', '행신', '능곡', '대곡',
       '곡산', '백마', '풍산', '일산', '탄현', '야당', '운정', '금릉', '금촌', '월롱', '파주', '문산']
train_list = ['K5001', 'K5002', 'K5003', 'K5004', 'K5005', 'K5006', 'K5007', 'K5008', 'K5009', 'K5010', 'K5011', 'K5012'
    ,'K5013', 'K5014', 'K5015', 'K5016', 'K5017', 'K5018', 'K5019', 'K5020', 'K5021', 'K5022', 'K5023', 'K5024', 'K5025', 'K5026'
    , 'K5027', 'K5028','K5029', 'K5030','K5031', 'K5032', 'K5033', 'K5034', 'K5035', 'K5036', 'K5037', 'K5038', 'K5039', 'K5040', 'K5041'
    , 'K5042', 'K5043', 'K5044', 'K5045', 'K5046', 'K5047', 'K5048', 'K5049', 'K5050', 'K5051', 'K5052', 'K5053', 'K5054'
    , 'K5055', 'K5056', 'K5057', 'K5058', 'K5059', 'K5060', 'K5061', 'K5062', 'K5063', 'K5064', 'K5065', 'K5066', 'K5067'
    , 'K5068', 'K5069', 'K5070', 'K5071', 'K5072', 'K5073', 'K5074', 'K5075', 'K5076', 'K5077', 'K5078', 'K5079', 'K5080'
    , 'K5081', 'K5082', 'K5083', 'K5084', 'K5085', 'K5086', 'K5087', 'K5088', 'K5089', 'K5090', 'K5091', 'K5092', 'K5093'
    , 'K5094', 'K5095', 'K5096', 'K5097', 'K5098', 'K5099', 'K5100', 'K5101', 'K5102', 'K5103', 'K5104', 'K5105', 'K5106'
    , 'K5107', 'K5108', 'K5109', 'K5110', 'K5111', 'K5112', 'K5113', 'K5114', 'K5115', 'K5116', 'K5117', 'K5118', 'K5119'
    , 'K5120', 'K5121','K5122', 'K5123', 'K5124', 'K5125', 'K5126', 'K5127', 'K5128', 'K5129', 'K5130','K5131', 'K5132', 'K5133', 'K5134'
    , 'K5135', 'K5136', 'K5137', 'K5138', 'K5139', 'K5140', 'K5141', 'K5142', 'K5143', 'K5144', 'K5145', 'K5146', 'K5147'
    , 'K5148', 'K5149', 'K5150', 'K5151', 'K5152', 'K5153', 'K5154', 'K5155', 'K5156', 'K5157', 'K5158', 'K5159', 'K5160'
    , 'K5161', 'K5162', 'K5163', 'K5164', 'K5165', 'K5166', 'K5167', 'K5168', 'K5170', 'K5171', 'K5231', 'K5246', 'K5272'
    , 'K5301', 'K5302', 'K5303', 'K5304', 'K5701', 'K5702', 'K5703', 'K5704', 'K5705', 'K5706', 'K5707', 'K5708', 'K5851'
    , 'K5852', 'K5853', 'K5854']

#print(data[1])
#print(len(data['열차번호']))

holidays = [datetime(2020,10,9),datetime(2020,10,3),datetime(2020,10,2),datetime(2020,10,1),datetime(2020,9,30),datetime(2020,8,17),datetime(2020,4,15),datetime(2020,5,5),datetime(2020,4,30),datetime(2020,3,1),datetime(2020,1,27),datetime(2020,1,26),datetime(2020,1,25),datetime(2020,1,24),datetime(2020,1,1)] # 긁어올 날 안에 일요일 토요일 제외 공휴일이 있다면 표시해줘야함

AD = []

data = pd.ExcelFile("09.xlsx").parse('0901')

# 열차번호 운행일자 주운행선 시발역 종착역 역 계획출발시각 계획도착시각 실제출발시각 실제도착시각
temp_a = []
temp_b = []
current_train = data['열차번호'][0]
current_date = data['운행일자'][0]
for i in range(len(data['열차번호'])):
    if(data['열차번호'][i][1]!='5'):
        continue
    if(data['열차번호'][i]!=current_train):
        AD.append(temp_a+temp_b)
        current_train = data['열차번호'][i]
        current_date = str(data['운행일자'][i])
        date = datetime(int(current_date[0:4]),int(current_date[4:6]),int(current_date[6:8]))
        holiday = 0
        if date in holidays:
            holiday = 1
        ud = int(current_train[4])%2
        temp_a = [current_train,date.weekday(),holiday,data['시발역'][i],data['종착역'][i],ud]
        temp_b = [None]*53
        continue
    current_target = str(data['계획도착시각'][i])
    current_real = str(data['실제도착시각'][i])
    try:
        target = int(current_target[8:10])*3600 + int(current_target[10:12])*60 + int(current_target[12:14])
        real = int(current_real[8:10])*3600+ int(current_real[10:12])*60+ int(current_real[12:14])
        delay=real-target
        if delay>12*3600:
            delay = delay-24*3600
            print('up')
        if delay<-12*3600:
            delay = delay+24*3600
            print('down')
        if abs(delay)>2000:
            print('delay :'+str(delay))
        temp_b[station_list_n.index(data['역'][i])] = delay
    except:
        print(current_target)
        print(current_real)
        continue

AD.remove([])


save = pd.DataFrame(AD)
save.to_csv("gagonged_data_09.csv")