# A3C main
# coded by St.Watermelon

## A3C 에이전트를 학습하고 결과를 도시하는 파일

# 필요한 패키지 임포트
from a3c_learn import A3Cagent

def main():

    max_episode_num = 500  # 최대 에피소드 설정
    env_name = 'Pendulum-v1'  # 환경으로 OpenAI Gym의 pendulum-v0 설정
    agent = A3Cagent(env_name) # A3C 에이전트 객체
    # 학습 진행
    agent.train(max_episode_num)
    # 학습 결과 도시
    agent.plot_result()

if __name__=="__main__":
    main()
