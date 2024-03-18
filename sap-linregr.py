import numpy, pandas as pd
import matplotlib, matplotlib.pyplot as plt
import sklearn.linear_model as lm

# 데이터를 읽어들인다.
sap = pd.read_csv("sapXXI.csv").set_index("Date")

# “선형적으로 보이는” 부분을 선택한다.
sap.index = pd.to_datetime(sap.index)
sap_linear = sap.ix[sap.index > pd.to_datetime('2009-01-01')]

# 모델을 준비하고 학습시킨다.
olm = lm.LinearRegression()
X = numpy.array([x.toordinal() for x in sap_linear.index])[:, numpy.newaxis]
y = sap_linear['Close']
olm.fit(X, y)

# 예측을 수행한다.
yp = [olm.predict(x.toordinal())[0] for x in sap_linear.index]

# 모델을 평가한다.
olm_score = olm.score(X, y)

# 플로팅 스타일을 선택한다.
matplotlib.style.use("ggplot")

# 두 데이터셋을 시각화한다.
plt.plot(sap_linear.index, y)
plt.plot(sap_linear.index, yp)

# 플롯을 꾸민다.
plt.title("OLS Regression")
plt.xlabel("Year")
plt.ylabel("S&P 500 (closing)")
plt.legend(["Actual", "Predicted"], loc="lower right")
plt.annotate("Score=%.3f" % olm_score, 
             xy=(pd.to_datetime('2010-06-01'), 1900))

plt.savefig("sap-linregr.pdf")
