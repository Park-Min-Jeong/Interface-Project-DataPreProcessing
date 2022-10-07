# InterfaceProject-DataPreProcessing
인터페이스 개발 프로젝트 데이터 전처리 _from 2022-10-06_

## py 파일
### library 확인
- bs4, lxml, pandas
- 없으면 pip로 설치

### 번호 붙은 파일
- 번호 순서 대로 실행
- 같은 번호 안에서는 실행 순서 상관 없음
- 6번 실행 전에 utils 폴더 안의 _filtering.py_ 파일을 맨 아래 행 _print(len(filter))_ 주석 해제하고 실행해서 에러 여부 확인


## utils 폴더
### 파일 목록
- _variables.py_
  - 전역적으로 사용되는 변수
- _basic.py_
  - 기본적인 함수
- _crawling.py_
  - 크롤링을 수행해서 데이터프레임을 만드는 함수
- _filtering.py_
  - 필터링 조건을 만들고 수행하는 함수


## data 폴더
### 데이터
- _heritage.py_
  - 문화재 정보
  - 코드북: https://docs.google.com/spreadsheets/d/1FOBmhzk1bs44TGthrKMzvheAOIHWQlEs0smfZi9grUA/edit?usp=sharing

### DB 포함 X
- raw 폴더 안에 있는 파일
- ccbaLcto 폴더 안에 있는 파일
  - _1 ccbaLcto_code.py_ 실행 결과 저장
  - 시도별 시군구 코드 저장


## 데이터 클리닝
### region_df
- __Lcto=="00" 제거__
  - Lcto: 시군구코드
  - "00": 해당 지역 전체 
  - 중복된 정보이므로 제외
- 2 raw_csv_region.py에서 수행

### period_df
- __Pcd1.isnull() or Pcd1=="60" or Pcd1=="00" 제거__
  - Pcd1: 시대코드
  - isnull(): 결측값
  - "60": 시대미상
  - "00": 선사시대 이전
  - 6 cleaning_data.py -- filtering_df(df) -- making_filter() -- filter_location_period()에서 수행
- __Pcd1=="01" or Pcd1=="10" 수정__
  - Pcd1: 시대코드
  - "01": 선사시대
  - "10": 삼국시대
  - 세부 시대로 변경
  - 6 cleaning_data.py에서 수행

### location_df
- __longitude=="0" or latitude=="0" 삭제__
  - longitude: 경도, latitude: 위도
  - "0": 누락된 정보
  - 6 cleaning_data.py -- filtering_df(df) -- making_filter() -- filter_location_period()에서 수행
- __duplicated [longitude, latitude] 삭제__
  - 위도와 경도가 같은 장소에 있는 경우
  - 6 cleaning_data.py -- filtering_df(df) -- making_filter() -- filter_location()

### kind_df
- __"Kdcd" not in ["11", "12", "13"] 삭제__
  - "11": 국보
  - "12": 보물
  - "13": 사적
  -  6 cleaning_data.py -- filtering_df(df) -- making_filter() -- filter_kind()에서 수행

### 결과
- 제거: 13674개
- 나머지: 1328개