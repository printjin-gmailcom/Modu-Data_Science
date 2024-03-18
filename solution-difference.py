import numpy as np

# 테스트용 데이터를 준비한다.
array = np.random.binomial(5, 0.5, size=100)

# 슬라이싱과 브로드캐스팅을 사용해 미분한다!
diff = array[1:] - array[:-1]
