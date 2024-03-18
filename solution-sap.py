import pandas as pd
from scipy.stats import pearsonr

# 데이터를 읽어들인다.
sap = pd.read_csv("sapXXII.csv").set_index("Date")

# 통계 지표를 계산하고 출력한다.
print("Mean:", sap["Close"].mean())
print("Standard deviation:", sap["Close"].std())
print("Skewness:", sap["Close"].skew())
print("Correlation:\n", sap[["Close", "Volume"]].corr())
_, p = pearsonr(sap["Close"], sap["Volume"])
print("p-value:", p)
