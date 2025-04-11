# REINFORCE Algorithm
*[코드 바로 보기: cartpole_r.ipynb](https://github.com/Y00NSJ/RL/blob/main/REINFORCE/implement/cartpole_r.ipynb)*
## 기본 구조
### 목적
Cartpole-v1 from OpenAI Gym
<br>
![cart_pole](https://github.com/user-attachments/assets/30cc97a7-a0b1-4549-b321-301017a0fe1b)
<br>
[출처](https://www.gymlibrary.dev/environments/classic_control/cart_pole/)

### Agent 클래스의 기능 구성
1. `build_model` 함수 호출 -> 모델 생성: 사용자 정의 비용 함수(`train_step`) 사용
2. 생성한 Agent 클래스에서 `train` 함수 호출해 학습 시작
3. `make_memory` 함수 통해 프로그램을 반복적으로 호출함으로써 경험 쌓고 정보 수집
4. 에피소드 종료 후, 수집한 정보를 모델 학습에 사용
  - 학습 전, 수집 정보 중 reward를 가공: `discount_rate` 적용
5. {경험 누적 -> 모델 학습} 과정을, 사전에 정해 놓은 에피소드의 수만큼 반복해 모델 학습 진행

## 특징
- 하나의 에피소드 종료 후 그동안 수집한 데이터를 모두 삭제
- 인공신경망에서 나온 정책 사용 => 확률적으로 행동 선택

## 결과 분석
- `rewards_avg` : 누적된 에피소드 전체에 대한 평균 보상 => 전반적 학습 성과의 지표
- `moving_avg` : 최근 N개의 에피소드에 대한 평균 보상 => 최근 학습 성과의 지표
