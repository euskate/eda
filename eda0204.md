## 20. 2. 4.
### 서울시 구별 인구현황 및 CCTV 현황 분석
### 실습 -> 부산시

- 천단위 콤마 변환
  - [링크](https://rfriend.tistory.com/463)
  - (1) pd.read_csv() 에서 thousands = ',' 옵션으로 천 단위 자리수 구분 콤마 없애고 불러오기
  - (2) DataFrame의 문자열 DataFrame.column.str.replace(',', '').astype('int64') 메소드를 이용하여 변환하기
  - (3) PostgreSQL, Greenplum DB에서 천 단위 자리수 구분 콤마 없애기

- 그래프 타이팅
  - plt.tight_layout()

- 한글 처리
```py
# 한글처리
import platform
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':    # 맥
    font_list_mac = fm.OSXInstalledFonts()
    font_name = 'AppleGothic'
elif platform.system() == 'Linux': # 리눅스
    font_name = 'NanumGothic'
elif platform.system() == 'Windows': # 윈도우
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
else:
    print('알수없는 시스템. 미적용')

rc('font', family=font_name)
```

