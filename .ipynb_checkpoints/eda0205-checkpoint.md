### 02. 05.
- 기록 방법
  - 블로그
  - [notion](https://www.notion.so/)
  - onenote...
  - [github_io](https://pages.github.com/) 

- 쥬피터 노트북 특수명령어
  - !
  - %
  - ? : 도움말 보기

- 제플린.. 알아보기(쥬피터 노트북 비슷)

- df.sample() : 랜덤하게 가져오기

- 연도, 월별 컬럼명 합쳐주는 반복문!
  - eda0205.md, 후반부에서 호가인
```py
# 컬럼을 새로 만들어 주기 위해 0번째와 1번째 행을 합쳐준다.
for i, y in enumerate(year):
    if i > 2 and i < 15:
        year[i] = ' '.join(['2014년', month[i]])
    elif i >= 15:
        year[i] = ' '.join(['2015년', month[i]])
    elif i == 2 :
        year[i] = ' '.join([year[i], month[i]])
    elif i == 1:
        year[i] = '시군구'
```

- 내일 시험 본다. 오전에 복습, 오전 공부 오후 시험


- pandas는 numpy 기반으로 한다.
- numpy 속도는 python 보다 빠름.


- ADsP
- p-value :  유의수준  0.05 이하면 유의하다.
- 귀무가설 : 귀무가설은 기각되야 좋다.
- R-squared 결정계수 :

    - 전진선택
    - 후진소거
    - 단계선택


- 정상성 이해하기


- 데이터 마이닝
  - 지도학습
  - 비지도학습 알기


- 성과분석 별표 다섯개!