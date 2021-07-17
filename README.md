# open_API_practice
- 지역 아파트 매매 실 거래가를 open API를 사용하여 구현해보았다.

- 실행 방법<br>
    1. 마지막 for문에 원하는 기간을 입력한다.<br> 

    2. 66번째 줄의 df = searchByRegionYM(i,'[지역코드]') 부분에 https://github.com/drtagkim/kor_gg_code/blob/master/region_code5.csv 를 참고하여 원하는 지역의 코드를 넣는다.
    <br>
    <br>
    EX ) 서정동의 2021-04~2021-05 기간 아파트 매매 실거래가
        ```python 
            import time
            sum = pd.DataFrame()
            for i in range(202104, 202105):#날짜작성
                df = searchByRegionYM(i'41220')#지역코드작성 
                sum = sum.append(df)
                time.sleep(10)
         ```