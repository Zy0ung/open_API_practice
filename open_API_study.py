import requests
from bs4 import BeautifulSoup
import pandas as pd

api_key="8DxiEK3iVFNABt2UOZAQNb%2FNZoEFxvTQrDHSW9XZc3zdwryKF9kOJNwMfji2lcr5bTh4GSdNI3OIpVLkgjHZqg%3D%3D"

def searchByRegionYM(deal_ymd,lawd_code): #년월, 지역코드(시군구 5자리)
    numOfRows = '10000' # 한번 노출 시 불러들이는 거래정보 량
    pageNo = '1' # 시작 페이지... 1회 호출에 10000건이 넘을 경우 다음페이지로 다시 호출 해야 함. 
    
    url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev?LAWD_CD=%s&DEAL_YMD=%s&ServiceKey=%s&numOfRows=%s&pageNo=%s' %(lawd_code, deal_ymd, api_key, numOfRows, pageNo)
    res = requests.get(url)
    
    soup = BeautifulSoup(res.text,'lxml-xml')
    it = soup.select('item')
    
    rows = []
    for node in it:
        try:
            n_serialNm = node.find('일련번호').text # 새로 생긴 단지의 경우 일련번호 없는 단지 있음. 
        except:
            n_serialNm =''
        
        try:
            n_add1 = node.find('지번').text # 지번이 없는 단지도 있음. 
        except:
            n_add1 = ''
        
        n_buildYear = node.find('건축년도').text
        n_dong = node.find('법정동').text
        n_aptName = node.find('아파트').text
        n_jySize = node.find('전용면적').text
        n_floor = node.find('층').text
        n_price = node.find('거래금액').text 
        n_tradeYear = node.find('년').text
        n_tradeMonth = node.find('월').text
        n_tradeDay = node.find('일').text
        n_siguCode = node.find('법정동시군구코드').text
        n_dongCode = node.find('법정동읍면동코드').text
        n_tradeYM = n_tradeYear +'-'+n_tradeMonth.rjust(2,'0')
        rows.append({'serialNm':n_serialNm,
                     'tradeYM':n_tradeYM,
                     'tradeDay':n_tradeDay,
                     'buildYear':n_buildYear,
                     'dong':n_dong,
                     'aptName':n_aptName,
                     'jySize':n_jySize,
                     'floor':n_floor,
                     'price':n_price,
                     'siguCode':n_siguCode,
                     'dongCode':n_dongCode,
                     'add1':n_add1,
                     })
        
    columns = ['serialNm','tradeYM','tradeDay','buildYear','dong','aptName','jySize','floor','price', 'siguCode', 'dongCode', 'add1' ]
    df = pd.DataFrame(rows, columns= columns)
    df['price'] = pd.to_numeric(df['price'].str.replace(',','')) # 특수 문자 바꾸기
    return df
# 지역코드 
# https://github.com/drtagkim/kor_gg_code/blob/master/region_code5.csv 참조

# 2021년 4월 ~ 5월 서정동 전체 아파트 거래
import time
sum = pd.DataFrame()
for i in range(202104, 202105):
    df = searchByRegionYM(i,'41220') 
    sum = sum.append(df)
    time.sleep(10)
    
print(sum)
