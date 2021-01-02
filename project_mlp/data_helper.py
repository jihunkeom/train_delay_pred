import pandas as pd
import numpy as np

station_list = ['지평', '용문', '원덕', '양평', '오빈', '아신', '국수', '신원',
       '양수', '운길산', '팔당', '도심', '덕소', '1양정', '도농', '구리', '1양원', '망우', '상봉',
       '중랑', '회기', '청량리', '왕십리', '응봉', '옥수', '한남', '서빙고', '이촌', '용산', '효창공',
       '공덕', '서강대', '홍대입', '가좌', '디엠시', '수색', '화전', '강매', '행신', '능곡', '대곡',
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

up_train = ['K5002', 'K5004', 'K5006', 'K5008', 'K5010', 'K5012', 'K5014', 'K5016', 'K5018', 'K5020', 'K5022', 'K5024', 'K5026', 'K5028', 'K5030', 'K5032', 'K5034', 'K5036', 'K5038', 'K5040', 'K5042', 'K5044', 'K5046', 'K5048', 'K5050', 'K5052', 'K5054', 'K5056', 'K5058', 'K5060', 'K5062', 'K5064', 'K5066', 'K5068', 'K5070', 'K5072', 'K5074', 'K5076', 'K5078', 'K5080', 'K5082', 'K5084', 'K5086', 'K5088', 'K5090', 'K5092', 'K5094', 'K5096', 'K5098', 'K5100', 'K5102', 'K5104', 'K5106', 'K5108', 'K5110', 'K5112', 'K5114', 'K5116', 'K5118', 'K5120', 'K5122', 'K5124', 'K5126', 'K5128', 'K5130', 'K5132', 'K5134', 'K5136', 'K5138', 'K5140', 'K5142', 'K5144', 'K5146', 'K5148', 'K5150', 'K5152', 'K5154', 'K5156', 'K5158', 'K5160', 'K5162', 'K5164', 'K5166', 'K5168', 'K5170', 'K5246', 'K5272', 'K5302', 'K5304', 'K5702', 'K5704', 'K5706', 'K5708', 'K5852', 'K5854']
down_train = ['K5001', 'K5003', 'K5005', 'K5007', 'K5009', 'K5011', 'K5013', 'K5015', 'K5017', 'K5019', 'K5021', 'K5023', 'K5025', 'K5027', 'K5029', 'K5031', 'K5033', 'K5035', 'K5037', 'K5039', 'K5041', 'K5043', 'K5045', 'K5047', 'K5049', 'K5051', 'K5053', 'K5055', 'K5057', 'K5059', 'K5061', 'K5063', 'K5065', 'K5067', 'K5069', 'K5071', 'K5073', 'K5075', 'K5077', 'K5079', 'K5081', 'K5083', 'K5085', 'K5087', 'K5089', 'K5091', 'K5093', 'K5095', 'K5097', 'K5099', 'K5101', 'K5103', 'K5105', 'K5107', 'K5109', 'K5111', 'K5113', 'K5115', 'K5117', 'K5119', 'K5121', 'K5123', 'K5125', 'K5127', 'K5129', 'K5131', 'K5133', 'K5135', 'K5137', 'K5139', 'K5141', 'K5143', 'K5145', 'K5147', 'K5149', 'K5151', 'K5153', 'K5155', 'K5157', 'K5159', 'K5161', 'K5163', 'K5165', 'K5167', 'K5171', 'K5231', 'K5301', 'K5303', 'K5701', 'K5703', 'K5705', 'K5707', 'K5851', 'K5853']
#data는 순서대로 열차번호, 요일, 공휴일, 시발역, 종착역, 상/하행, 역별 지연정보

#X는 one hot incoding으로 모두 concat된 입력쌍, 순서대로 열차, 요일, 공휴일, 시발역, 종착역, 상/하행력, 정차역
#Y는 지연정보
#RNN 학습을 위해 입력값을 한열차당 데이터로 묶어서 표현, 한 인풋당 길이 357, 역이 53개 인 2차원 데이터임

# DATA EXAMPLE
# 하나의 x input [0, 1, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, ..... 0, 0, 0, 0, 0,0, 0, 0, 0 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
# RNN의 placeholder에 집어넣을 X input [[0,1,0,0,0,0,0...],[0,0,1,0,0,0,0,0,...],[0,0,0,1,0,0,0....],...]
# 하나의 y input 13(초)
# RNN의 placeholder에 집어넣을 Y input [14,2,53,3,1,0,...]


#path는 train table 경로, count는 default all로 전부 불러오며 설정할시 count에 설정한 줄 수만큼 불러옴, 간단히 데이터 내용 보고싶을때 사용하려고 만듬
# default(all)로 불러오면 train할떄 시간이 좀 걸릴 수 있으니 조금씩 늘려가며 간보는걸 추천드립니다. 전체 데이터 수가 약 37000개 정도 됩니다.

# default version = 0, X 역별 한개 길이 357
# 시작역, 종착역 정보제거 version = 1, X 역별 한개 길이 251
# 시작역, 종착역 정보제거, 열차를 상/하행별로 순서만 반영 version = 2,X 역별 한개 길이 157
def readTraindata(path,ver=0,count='all'):
    if ver == 0:
        return readTraindata0(path,count)
    elif ver ==1:
        return readTraindata1(path,count)
    elif ver ==2:
        return readTraindata2(path,count)
    return print('input error')


def readTraindata0(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path).drop(['Unnamed: 0'], axis=1)
    else:
        df = pd.read_csv(path).drop(['Unnamed: 0'], axis=1)[:count]
    x=[]
    y=[]
    for item in df.values:
        x_fraction = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +oneHot("station",getStationNum(item[3]))+oneHot('station',getStationNum(item[4]))+[item[5]]
        temp = item[6:]
        x_f = [];
        if item[5] == 0:
            for i in range(len(temp)):
                x_f.append(x_fraction + oneHot('station', i))
            y.append(factorize(list(temp)))
        elif item[5] == 1:
            for i in range(len(temp)):
                x_f.append(x_fraction + oneHot('station', i, inverse=True))
            y_f=list(temp)
            y_f.reverse()
            y.append(factorize(y_f))
        x.append(x_f)
    return x, y

def readTraindata1(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path).drop(['Unnamed: 0'], axis=1)
    else:
        df = pd.read_csv(path).drop(['Unnamed: 0'], axis=1)[:count]
    x=[]
    y=[]
    for item in df.values:
        x_fraction = oneHot('train', getTrainNum(item[0])) + oneHot('weekdays', item[1]) + [item[2]] + [item[5]]
        temp = item[6:]
        x_f = [];
        if item[5] == 0:
            for i in range(len(temp)):
                x_f.append(x_fraction + oneHot('station', i))
            y.append(factorize(list(temp)))
        elif item[5] == 1:
            for i in range(len(temp)):
                x_f.append(x_fraction + oneHot('station', i, inverse=True))
            y_f=list(temp)
            y_f.reverse()
            y.append(factorize(y_f))
        x.append(x_f)
    return x, y

def readTraindata2(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path).drop(['Unnamed: 0'], axis=1)
    else:
        df = pd.read_csv(path).drop(['Unnamed: 0'], axis=1)[:count]
    x=[]
    y=[]
    for item in df.values:
        if item[5] == 0:
            train_onehot = oneHot('train_ud',getTrainNum(item[0],0))
        else:
            train_onehot = oneHot('train_ud',getTrainNum(item[0],1))
        x_fraction = train_onehot +oneHot('weekdays',item[1])+[item[2]]+[item[5]]
        temp = item[6:]
        x_f = [];
        if item[5] == 0:
            for i in range(len(temp)):
                x_f.append(x_fraction + oneHot('station', i))
            y.append(factorize(list(temp)))
        elif item[5] == 1:
            for i in range(len(temp)):
                x_f.append(x_fraction + oneHot('station', i, inverse=True))
            y_f=list(temp)
            y_f.reverse()
            y.append(factorize(y_f))
        x.append(x_f)
    return x, y

def read2(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x=[]; y=[]
    for item in df.values:
        if (item[7]>=53):
            continue
        x_f = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +oneHot("station",getStationNum(item[3]))+oneHot('station',getStationNum(item[4]))+[item[5]]+oneHot('station',item[6])+oneHot('station',item[7])+[item[8]];
        x.append(x_f)
        y.append(item[9])
    return np.array(x),np.array(y)

def read3(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x=[]; y=[]
    for item in df.values:
        if (item[7]>=53):
            continue
        x_f = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +[item[5]]+[np.absolute(item[7]-item[6])]+[item[8]];
        x.append(x_f)
        y.append(item[9])
    return np.array(x),np.array(y)

def read4(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x1=[];x2=[]; y=[]
    for item in df.values:
        if (item[7]>=53):
            continue
        x_f = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +[item[5]]+oneHot('station',item[6])+oneHot('station',item[7]);
        x_f_1 = item[8]
        x1.append(x_f)
        x2.append(x_f_1)
        y.append(item[9])
    return np.array(x1),np.array(x2),np.array(y)

def read5(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x=[]; y=[]
    for item in df.values:
        if (item[6]>=53)or(item[7]>=53)or(item[8]>=53):
            print(item)
            continue
        x_f = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +[item[5]]+oneHot('station',item[6])+oneHot('station',item[7])+oneHot('station',item[8])+[item[9]]+[item[11]];
        x.append(x_f)
        y.append(item[10])
    return np.array(x),np.array(y)

def read6(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x=[]; y=[]
    for item in df.values:
        if (item[6]>=53)or(item[7]>=53)or(item[8]>=53):
            print(item)
            continue
        x_f = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +[item[5]]+oneHot('station',item[6],value=item[9])+oneHot('station',item[7])+oneHot('station',item[8],value=item[11]);
        x.append(x_f)
        y.append(item[10])
    return np.array(x),np.array(y)

def read7(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x=[]; y=[]
    for item in df.values:
        if (item[6]>=53)or(item[7]>=53)or(item[8]>=53):
            print(item)
            continue
        x_f = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +[item[5]]+oneHot('station',item[6],value=item[9])+oneHot('station',item[7])+oneHot('station',item[8],value=item[11]);
        x.append(x_f)
        y.append([item[9],item[10],item[11]])
    return np.array(x),np.array(y)

def read8(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x=[]; y=[]
    for item in df.values:
        if (item[6]>=53)or(item[7]>=53)or(item[8]>=53):
            print(item)
            continue
        x_f = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +[item[5]]+oneHot('station',item[6])+oneHot('station',item[7])+oneHot('station',item[8])+[item[9]]+[item[11]];
        x.append(x_f)
        y.append([item[9],item[10],item[11]])
    return np.array(x),np.array(y)

def read9(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x1=[];x2=[];x3=[]; y=[]
    for item in df.values:
        if (item[6]>=53)or(item[7]>=53)or(item[8]>=53):
            print(item)
            continue
        x_f1 = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +[item[5]]
        x_f2 = [oneHot('station',item[6]),oneHot('station',item[7]),oneHot('station',item[8])]
        x_f3 = [item[9]]+[item[11]];
        x1.append(x_f1)
        x2.append(x_f2)
        x3.append(x_f3)
        y.append(item[10])
    return np.array(x1),np.array(x2),np.array(x3),np.array(y)

def readTraindataMasked(path,count='all'):
    if count == 'all':
        df = pd.read_csv(path)
    else:
        df = pd.read_csv(path)[:count]
    x=[]
    y=[]
    for item in df.values:
        x_fraction = oneHot('train',getTrainNum(item[0]))+oneHot('weekdays',item[1])+[item[2]]\
                   +oneHot("station",getStationNum(item[3]))+oneHot('station',getStationNum(item[4]))+[item[5]]
        temp = item[6:]
        x_f = [];
        if item[5] == 0:
            for i in range(len(temp)):
                if np.isnan(temp[i]):
                    x_f.append([0]*357)
                else:
                    x_f.append(x_fraction + oneHot('station', i))
            y.append(factorize(list(temp)))
        elif item[5] == 1:
            for i in range(len(temp)):
                if np.isnan(temp[i]):
                    x_f.append([0]*357)
                else:
                    x_f.append(x_fraction + oneHot('station', i, inverse=True))
            y_f=list(temp)
            y_f.reverse()
            y.append(factorize(y_f))
        x.append(x_f)
    return x, y





def factorize(y):
    for i in range(len(y)):
        if np.isnan(y[i]):
            y[i] = 0
    return [[item] for item in y]


def oneHot(type,val,inverse=False,value=None):
    if type == 'train':
        long = 189
    elif type == 'station':
        long = 53
    elif type == 'weekdays':
        long = 7
    elif type == 'train_ud':
        long = 95
    a = [0] * (long)
    if value==None:
        value = 1
    if inverse:
        a[long-val-1] = value
    else:
        a[val] = value
    return a




def getStationNum(name):
    return(station_list.index(name))

def getTrainNum(name,ud=None):
    if ud==0:
        return(up_train.index(name))
    elif ud ==1:
        return(down_train.index(name))
    return(train_list.index(name))

def getStationName(num):
    return(station_list[num])

def getTrainName(num):
    return(train_list[num])

a,b,c,_ = read9('train3set.csv',20)
print(a.shape)
print(b.shape)
print(c.shape)


# data=pd.read_csv('test3set_rb.csv')
# print(data.shape)
# abst=[]
# cor10 = []
# cor15 = []
# cor30 = []
# cor60 = []
# for item in data.values:
#     est = item[9]+(item[11]-item[9])*(item[7]-item[6])/(item[8]-item[6])
#     val = abs(est - item[10])
#     abst.append(val)
#     if val <=10:
#         cor10.append(1)
#     else:
#         cor10.append(0)
#     if val <=15:
#         cor15.append(1)
#     else:
#         cor15.append(0)
#     if val <=30:
#         cor30.append(1)
#     else:
#         cor30.append(0)
#     if val <=60:
#         cor60.append(1)
#     else:
#         cor60.append(0)
#
# print(np.mean(abst))
# print(np.mean(cor10))
# print(np.mean(cor15))
# print(np.mean(cor30))
# print(np.mean(cor60))


# data=pd.read_csv('train3setV2.csv')
#
# abst=[]
#
# for item in data.values:
#     est = item[9]+(item[11]-item[9])*(item[7]-item[6])/(item[8]-item[6])
#     abst.append(abs(est-item[10]))
#
# print(np.mean(abst))
#
#
# data=pd.read_csv('train3setOrderRand.csv')
# abst=[]
#
# for item in data.values:
#     est = item[9]+(item[11]-item[9])*(item[7]-item[6])/(item[8]-item[6])
#     abst.append(abs(est-item[10]))
#
# print(np.mean(abst))