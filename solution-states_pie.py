import pandas as pd
import matplotlib, matplotlib.pyplot as plt

def initial(word):
    return word[0]

# 주 이름을 읽어들인다(데이터 출처는 어디든 좋다!).
states = pd.read_csv("states2.csv", 
                     names=("State", "Standard", "Postal", "Capital"))

# 플롯 스타일을 설정한다.
matplotlib.style.use("ggplot")

# 플로팅
plt.axes(aspect=1)
states.set_index('Postal').groupby(initial).count()['Standard'].plot.pie()
plt.title("States by the First Initial")
plt.ylabel("")

plt.savefig("states-pie.pdf")
