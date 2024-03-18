import matplotlib, matplotlib.pyplot as plt
import pickle, pandas as pd

# 앞에서 NIAAA 데이터 프레임을 pickle로 저장해 두었다.
alco = pickle.load(open("alco.pickle", "rb"))

# 플로팅에 쓸 데이터를 준비한다.
BEVERAGE = "Beer"
years = alco.index.levels[1]
states = ("New Hampshire", "Colorado", "Utah")

# 적절한 스타일을 고른다.
plt.xkcd()
matplotlib.style.use("ggplot")

# 차트를 그린다.
for state in states:
    ydata = alco.ix[state][BEVERAGE]
    plt.plot(years, ydata, "-o")
    # 화살표와 메모를 추가한다.
    plt.annotate(s="Peak", xy=(ydata.argmax(), ydata.max()),
                 xytext=(ydata.argmax() + 0.5, ydata.max() + 0.1),
                 arrowprops={"facecolor": "black", "shrink": 0.2})

# 레이블과 범례를 추가한다.
plt.ylabel(BEVERAGE + " consumption")
plt.title("And now in xkcd...")
plt.legend(states)

plt.savefig("pyplot-legend-xkcd.pdf")
