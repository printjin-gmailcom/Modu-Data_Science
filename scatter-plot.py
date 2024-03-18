import matplotlib, matplotlib.pyplot as plt
import pickle, pandas as pd

# 앞에서 NIAAA 데이터 프레임을 pickle로 저장해 두었다.
alco = pickle.load(open("alco.pickle", "rb"))

# 적절한 스타일을 고른다.
matplotlib.style.use("ggplot")

# 스캐터 플롯을 그린다.
STATE = "New Hampshire"
statedata = alco.ix[STATE].reset_index()
statedata.plot.scatter("Beer", "Wine", c="Year", s=100, cmap=plt.cm.autumn)

plt.title("%s: From Beer to Wine in 32 Years" % STATE)
plt.savefig("scatter-plot.pdf")

