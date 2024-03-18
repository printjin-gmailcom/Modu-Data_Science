# 필요한 라이브러리를 불러온다.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# 신호, 잡음, 그리고 "악기" 정보를 상수로 정의한다.
SIG_AMPLITUDE = 10; SIG_OFFSET = 2; SIG_PERIOD = 100
NOISE_AMPLITUDE = 3
N_SAMPLES = 5 * SIG_PERIOD
INSTRUMENT_RANGE = 9

# 사인 곡선을 구성하고 잡음을 섞어 넣는다.
times = np.arange(N_SAMPLES).astype(float)
signal = SIG_AMPLITUDE * np.sin(2 * np.pi * times / SIG_PERIOD) + SIG_OFFSET
noise = NOISE_AMPLITUDE * np.random.normal(size=N_SAMPLES)
signal += noise

# # 음역대를 벗어난 스파이크를 제거한다.
signal[signal > INSTRUMENT_RANGE] = INSTRUMENT_RANGE
signal[signal < -INSTRUMENT_RANGE] = -INSTRUMENT_RANGE



# 결과를 플롯(plot)으로 시각화한다.
matplotlib.style.use("ggplot")
plt.plot(times, signal)
plt.title("Synthetic sine wave signal")
plt.xlabel("Time")
plt.ylabel("Signal + noise")
plt.ylim(ymin = -SIG_AMPLITUDE, ymax = SIG_AMPLITUDE)

# 플롯을 저장한다.
plt.savefig("signal.pdf")
