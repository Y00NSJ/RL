# 다시 필요한 라이브러리 임포트 및 데이터 재불러오기
import pandas as pd
import matplotlib.pyplot as plt

# 파일 경로
file_data_parallel = "/mnt/data/데이터 병렬화 A3C 결과.txt"
file_gradient_parallel = "/mnt/data/그래디언트 병렬화 A3C 결과.txt"

# 파일 로딩
data_decentralized = pd.read_csv(file_data_parallel, header=None)
data_gradient = pd.read_csv(file_gradient_parallel, header=None)

# 컬럼명 지정
data_decentralized.columns = ["reward"]
data_gradient.columns = ["reward"]

# rolling 평균으로 smoothing
window = 10
data_decentralized["smoothed"] = data_decentralized["reward"].rolling(window).mean()
data_gradient["smoothed"] = data_gradient["reward"].rolling(window).mean()

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(data_decentralized["smoothed"], label="Data Parallel A3C (Smoothed)", alpha=0.8)
plt.plot(data_gradient["smoothed"], label="Gradient Parallel A3C (Smoothed)", alpha=0.8)
plt.xlabel("Episode")
plt.ylabel("Reward")
plt.title("Episode Reward Comparison: Data Parallel vs Gradient Parallel A3C")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()