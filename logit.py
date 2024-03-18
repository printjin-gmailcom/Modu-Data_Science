from scipy.stats import logistic
import numpy as np
import matplotlib, matplotlib.pyplot as plt

# 원하는 플로팅 스타일을 선택한다.
matplotlib.style.use("ggplot")

# 일부 다른 로직 곡선을 보여준다.
x = np.arange(-10, 10.1, 0.05)
scales = (0.01, 0.5, 1, 2)
for scale in scales:
    plt.plot(x, logistic.cdf(x, 0, scale))

# 플롯을 꾸민다.
plt.xlabel("x")
plt.ylabel("CDF(x)")
plt.title("Logistic function")
plt.ylim(ymin=-0.05, ymax=1.05)
plt.xlim(xmin=-10.05, xmax=10.05)
plt.legend(["Scale=%.2f" % scale for scale in scales], loc="lower right")

# 플롯을 저장한다.
plt.savefig("logit.pdf")
