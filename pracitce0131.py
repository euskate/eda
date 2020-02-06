
import urllib.request as ul
import json, datetime, time
import pandas as pd

def info():
    movieDate = time.strftime('%Y%m%d', time.localtime(time.time()))
    print(movieDate)
    cine=[{}]
    # movieDate = 20200130
    for i in range(0,30):
        datetime_obj = datetime.datetime.strptime(str(movieDate), "%Y%m%d")
        datetime_obj_tmp = datetime_obj - datetime.timedelta(days=1)
        # datetime_obj_tmp = datetime_obj - datetime.timedelta(weeks=1)
        # date -> str
        day = datetime_obj_tmp.strftime("%Y-%m-%d").split('-')
        movieDate = day[0]+day[1]+day[2]
        print(movieDate)
        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=66e652e1d2656b42f10d93c91e0295e4&targetDt={movieDate}"
        request = ul.Request(url)
        response = ul.urlopen(request)
        rescode = response.getcode()
        if(rescode == 200):
            responseData = response.read()
        print(rescode)
        result = json.loads(responseData)
        pre_result = result["boxOfficeResult"]
        pre_result1 = pre_result['dailyBoxOfficeList']
        # print(pre_result1)
        # 날짜, 영화이름, 누적 관객수
        for i in range(0, len(pre_result1)):
            pre_result1[i]['targetDt'] = movieDate
            cine.append(pre_result1[i])
        # print(cine)
        # 반복 함수 마지막에 날짜를 줄이는 함수를 사용한다.
        # str -> date
            
        # 1주일 씩 시간을 줄여간다.
  
        df = pd.DataFrame(cine)
        df = df[1:] # 첫행이 비어있음
        print(df)
    df.to_csv("cine.csv", index=False)

info()

