import pandas as pd, numpy as np
import sklearn.cluster, sklearn.preprocessing
import matplotlib, matplotlib.pyplot as plt

# 데이터를 읽어들인다.
mosn = pd.read_csv('mosn.csv', thousands=',',
                   names=('Name', 'Description', 'Date', 'Registered Users',
                          'Registration', 'Alexa Rank'))
columns = ['Registered Users', 'Alexa Rank']

# 데이터가 없거나 0이 있는 행을 제거한다.
good = mosn[np.log(mosn[columns]).notnull().all(axis=1)].copy()

# 클러스터링을 수행한다.
kmeans = sklearn.cluster.KMeans()
kmeans.fit(np.log(good[columns]))
good["Clusters"] = kmeans.labels_

# 어느 클러스터가 페이스북인가?
fb = good.set_index('Name').ix['Facebook']['Clusters']

# 적당한 플로팅 스타일을 선택한다.
matplotlib.style.use("ggplot")

# 결과를 출력한다.
ax = good.plot.scatter(columns[0], columns[1], c="Clusters", 
                       cmap=plt.cm.Accent, s=100)
plt.title("Massive online social networking sites")
plt.xscale("log")
plt.yscale("log")

# 가장 잘 나가는 서비스의 명칭을 표기한다.
def add_abbr(site):
    if site['Clusters'] == fb:
        _ = ax.annotate(site["Name"], site[columns], xytext=(1, 5), 
                        textcoords="offset points", size=8,
                        color="darkslategrey")
good.apply(add_abbr, axis=1)

plt.savefig("mosn.png")
