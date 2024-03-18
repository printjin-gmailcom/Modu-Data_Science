import os, pandas as pd
import urllib.request

# 상수를 정의한다.
SRC_HOST = "vincentarelbundock.github.io"
FILE = "lynx.csv"
SRC_NAME = SRC_HOST + "/Rdatasets/csv/datasets/" + FILE
CACHE = "cache"
DOC = "doc"

# 필요한 경우 디렉토리를 준비해둔다.
if not os.path.isdir(CACHE):
    os.mkdir(CACHE)
if not os.path.isdir(DOC):
    os.mkdir(DOC)

# 파일이 캐시되었는지 확인한다. 그렇지 않다면 캐시 처리한다.
if not os.path.isfile(CACHE + FILE):
    try:
        src = urllib.request.urlopen(SRC_NAME)
        lynx = pd.read_csv(src)
    except:
        print("Cannot access %f." % SRC_NAME)
        quit()
    # 데이터 프레임을 생성한다.
    lynx.to_csv(CACHE + FILE)
else:
    lynx = pd.read_csv(CACHE + FILE)

# decade 열을 추가한다.
lynx["decade"] = (lynx['time'] / 10).round() * 10

# 데이터를 집계하고 정렬한다.
by_decade = lynx.groupby("decade").sum()
by_decade = by_decade.sort_values(by="lynx", ascending=False)

# 결과를 저장한다.
by_decade["lynx"].to_csv(DOC + FILE)
