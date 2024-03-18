from pandas.tools.plotting import scatter_matrix
import matplotlib, matplotlib.pyplot as plt
import pickle, pandas as pd

# 앞에서 NIAAA 데이터 프레임을 pickle로 저장해 두었다.
alco = pickle.load(open("alco.pickle", "rb"))

# 적절한 스타일을 고른다.
matplotlib.style.use("ggplot")

# scatter matrix를 그린다.
STATE = "New Hampshire"
statedata = alco.ix[STATE].reset_index()
scatter_matrix(statedata[["Wine", "Beer", "Spirits"]],
               s=120, c=statedata["Year"], cmap=plt.cm.autumn)

plt.tight_layout()
plt.savefig("scatter-matrix.pdf")

