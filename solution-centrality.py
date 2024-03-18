import networkx as nx, community
import pandas as pd

# 네트워크를 임포트한다.
G = nx.read_adjlist(open("soc-Epinions1.txt", "rb"))

# 커뮤니티 구조를 추출하고 데이터 시리즈에 저장한다.
partition = pd.Series(community.best_partition(G))

# 10번째로 가장 큰 커뮤니티의 인덱스를 찾는다.
top10 = partition.value_counts().index[9]

# 10번째로 큰 커뮤니티를 추출한다.
# 노드 라벨이 문자열로 되어 있다는 것을 기억하자!
subgraph = partition[partition == top10].index.values.astype('str')
F = G.subgraph(subgraph)

# 네트워크 지표를 계산한다.
df = pd.DataFrame()
df["degree"] = pd.Series(nx.degree_centrality(F))
df["closeness"] = pd.Series(nx.closeness_centrality(F))
df["betweenness"] = pd.Series(nx.betweenness_centrality(F))
df["eigenvector"] = pd.Series(nx.eigenvector_centrality(F))
df["clustering"] = pd.Series(nx.clustering(F))

# 상관성을 계산한다.
print(df.corr())
