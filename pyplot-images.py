import matplotlib, matplotlib.pyplot as plt
import pickle, pandas as pd

# 앞에서 NIAAA 데이터 프레임을 pickle에 저장해 두었다.
alco = pickle.load(open("alco.pickle", "rb"))
del alco["Total"]
columns, years = alco.unstack().columns.levels

# 파일에서 축약된 주 이름을 읽어온다.
states = pd.read_csv("states.csv", index_col="State")

# 2009년을 기준으로 알코올 소비량을 정렬한다.
frames = [pd.merge(alco[column].unstack(), states,
                   left_index=True, right_index=True).sort_values(2009) 
          for column in columns]

# 데이터의 총 기간은 몇 년인가?
span = max(years) - min(years) + 1

# 적절해보이는 스타일을 선택한다.
matplotlib.style.use("ggplot")

STEP = 5
# subplot에 각 데이터 프레임을 시각화한다.
for pos, (draw, style, column, frame) in enumerate(zip(
        (plt.contourf, plt.contour, plt.imshow), # (1)
        (plt.cm.autumn, plt.cm.cool, plt.cm.spring), 
        columns, frames)):
    
    # 2개 행과 2개 열을 가진 subplot을 선택한다.
    plt.subplot(2, 2, pos + 1) # (2)

    # 데이터 프레임을 시각화한다.
    draw(frame[frame.columns[:span]], cmap=style, aspect="auto") # (3)

    # 플롯을 꾸민다.
    plt.colorbar() # (4)
    plt.title(column)
    plt.xlabel("Year")
    plt.xticks(range(0, span, STEP), frame.columns[:span:STEP])
    plt.yticks(range(0, frame.shape[0], STEP), frame.Postal[::STEP])
    plt.xticks(rotation=-17)

plt.tight_layout()
plt.savefig("pyplot-all.pdf")
#plt.show()
