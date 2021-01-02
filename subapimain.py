import signal
import sys
import json
import requests
import datetime
import time
from pytz import timezone

f = None

def collect(nowdate):
    url = "http://swopenAPI.seoul.go.kr/api/subway/696476646a6b697031303868626b7a4b/json/realtimePosition/0/50/경의중앙선"
    try:
        req = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(f'{nowdate} RequestsException:', e)
        return 1

    recv = json.loads(req.text)

    if 'errorMessage' in recv:
        msg = recv['errorMessage']
    else:
        msg = recv
    print(f"{nowdate} {msg['status']} {msg['code']} {msg['message']}")

    if msg['code'] != 'INFO-000':
        # Error!
        return 0

    rows = recv['realtimePositionList']
    f.write(f"{nowdate.strftime('%H:%M:%S.%f')}")
    for row in rows:
        f.write(f",{row['trainNo']},{row['statnNm']},{row['statnTnm']},{row['trainSttus']},{row['directAt']}")
    f.write("\n")

    return 0


def receive_signal(signum, stack):
    print(f"Signal received. Quit. (signum={signum})")
    if f is not None:
        f.close()
        f = None
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, receive_signal)
    signal.signal(signal.SIGINT, receive_signal)
    res = 0

    while True:
        nowdate = datetime.datetime.now(tz=timezone('Asia/Seoul'))
        if nowdate.time() >= datetime.time(hour=1) and nowdate.time() < datetime.time(hour=4):
            print('It\'s 1 ~ 4 AM. No trains. Quit.')
            if f is not None:
                f.close()
                f = None
            break
        else:
            if f is None:
                f = open(nowdate.strftime("%Y-%m-%d") + ".csv", "a+")
                f.write("시간,열차번호,현위치,행선지(종착역),진입(0)/도착(1),급행여부,열차번호,현위치,행선지(종착역),진입(0)/도착(1),급행여부\n")
            res = collect(nowdate)
            if res != 0:
                time.sleep(10)
                res = 0
            else:
                time.sleep(90)
