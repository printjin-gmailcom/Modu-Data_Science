from sklearn.ensemble import RandomForestRegressor
import pandas as pd, numpy.random as rnd
import matplotlib, matplotlib.pyplot as plt

# 데이터를 읽어들이고, 데이터셋을 2가지로 무작위 분리한다.
hed = pd.read_csv('Hedonic.csv')
selection = rnd.binomial(1, 0.7, size=len(hed)).astype(bool)
training = hed[selection]
testing = hed[-selection]

# 랜덤 포레스트 객체와 예측 변수 셋을 생성한다.
rfr = RandomForestRegressor()
predictors_tra = training.ix[:, "crim" : "lstat"]
predictors_tst = testing.ix[:, "crim" : "lstat"]

# 모델을 학습시킨다.
feature = "medv"
rfr.fit(predictors_tra, training[feature]) # (1)

# 적절한 플로팅 스타일을 선택한다.
matplotlib.style.use("ggplot")

# 예측 결과를 플롯에 시각화한다.
plt.scatter(training[feature], rfr.predict(predictors_tra), c="green",
            s=50) # (2)
plt.scatter(testing[feature], rfr.predict(predictors_tst), c="red") # (3)
plt.legend(["Training data", "Testing data"], loc="upper left")
plt.plot(training[feature], training[feature], c="blue")
plt.title("Hedonic Prices of Census Tracts in the Boston Area")
plt.xlabel("Actual value")
plt.ylabel("Predicted value")
plt.savefig("rfr.pdf")
