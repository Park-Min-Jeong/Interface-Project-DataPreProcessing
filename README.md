# InterfaceProject-DataPreProcessing
인터페이스 개발 프로젝트 데이터 전처리 from 2022-10-06

## py 파일
### library 확인
- bs4, lxml, pandas
- 없으면 pip로 설치

### 번호 붙은 파일
- 번호 순서 대로 실행
- 같은 번호 안에서는 실행 순서 상관 없음
- 5번 실행 전에 _utils_filter.py_ 파일을 맨 아래 행 _print(len(filter))_ 주석 해제하고 실행해서 에러 여부 확인

### 함수 모음
- _utils_basic.py_
  - 기본적인 함수와 변수
- _utils_raw.py_
  - raw data 만드는 함수
- _utils_filter.py_
  - 필터링 조건을 만들고 수행하는 함수


## ccbaLcto 폴더
- _1 ccbaLcto_code.py_ 실행 결과 저장
- 시도별 시군구 코드 저장
- _ccbaLcto_ccbaCtco.csv_ 


## data 폴더 
### DB 포함 X
- raw 폴더 안에 있는 파일
- _detail_request.csv_

### 코드북
- https://docs.google.com/spreadsheets/d/1FOBmhzk1bs44TGthrKMzvheAOIHWQlEs0smfZi9grUA/edit?usp=sharing

### 검색용
- _period.csv_
- _region.csv_

### 검색 예비용
- 혹시나 해서 남겨둠
- _kind.csv_
- _name.csv_

### marker 생성
- _location.csv_

### 문화재 정보
- _info.csv_


## 데이터 필터링
### region_df
- __Lcto=="00"__
  - Lcto: 시군구코드
  - "00": 해당 지역 전체 
  - 중복된 정보이므로 제외
- 2 raw_csv_region.py에서 수행

### period_df
- __Pcd1.isnull() or Pcd1=="60" or Pcd1=="00"__
  - Pct1: 시대코드
  - isnull(): 결측값
  - "60": 시대미상
  - "00": 선사시대 이전
- 5 filtering_data.py -- filtering(df) -- making_filter() -- filter_location_period()에서 수행

### location_df
- __longitude=="0" or latitude=="0"__
  - longitude: 경도, latitude: 위도
  - "0": 누락된 정보
- 5 filtering_data.py -- filtering(df) -- making_filter() -- filter_location_period()에서 수행

### info_df
- __"박물관" in Lcad or "미술관" in Lcad__
  - Lcad: 소재지 상세
- 박물관 혹은 미술관에 없는 문화재를 표기하고자 했기에 삭제
- 5 filtering_data.py -- filtering(df) -- making_filter() -- filter_info()에서 수행

### kind_df
- __"Kdcd" not in ["11", "12", "13"]__
  - "11": 국보
  - "12": 보물
  - "13": 사적
-  5 filtering_data.py -- filterinf(df) -- making_filter() -- filter_kind()에서 수행

### 결과
- 제거: 13453개
- 나머지: 1549개


### 수행하지 않은 조건
1. region_df ⇒ Ctco.isnull()
   * 2번과 동일한 결과

2. kind_df ⇒ Kdcd=="80"
   * 2번과 동일한 결과
