# 발표: A2C 크리틱 클래스 구현
![슬라이드1](https://github.com/user-attachments/assets/31cef1ba-6e5b-4e39-810b-a118b5e3bb9a)


## 구조
![슬라이드2](https://github.com/user-attachments/assets/b90c48c6-57d0-4919-a9e3-3a202914b7cb)

입력으로 수직축좌표/수평축좌표/각속도
Fully connected여서 파라미터의 개수가
현재 레이어의 노드수 * 이전 레이어의 노드수 + 바이어스 수
바이어스는 노드마다 하나씩 있으니까 현재 레이어의 노드수만큼
출력은 상태가치

## 크리틱 신경망 코드
앞 구조를 그대로 추상화한 클래스

![슬라이드3](https://github.com/user-attachments/assets/59f24e83-4c51-4c57-983c-b41bed1f98ae)
노드 수
활성함수는 ReLU

## 크리틱 신경망 학습
![슬라이드4](https://github.com/user-attachments/assets/570f7811-a7c8-4468-adde-61a858b31a4d)

그러니까, 크리틱 신경망의 파라미터인 화이를 업데이트하는 것.
상태에 대한 가치가, 이전 스텝에서 계산한 시간차 타깃과 가까워지도록 파라미터 업데이트

loss: 크리틱 신경망 출력값이랑 TD target 값의 오차==지금 신경망이 얼마나 틀렸는지
를, 가중치&바이어스들에 대해 미분 -> 가중치별로 loss 줄이려면 어느 방향으로 얼마나 이동해야 할까? 기울기를 제시

## 하이퍼파라미터
![슬라이드5](https://github.com/user-attachments/assets/fc9560bf-b721-4bd6-9afe-d9dbaaeabb78)

학습률:아담옵티마이저에 적용

## 시간차 타깃 계산
![슬라이드6](https://github.com/user-attachments/assets/29d17e84-c3c3-41a4-9211-3305dcf00a3c)

배치 동안 쌓인 각 샘플들의 시간차 타깃 계산
만약 그 샘플이 에피소드가 끝난 시점에 생성된 거면 다음 상태가 없으니까 보상 필요없고
그게 아니라면 다음 상태의 가치에 감가율곱한걸 더해야겠디

## 배치 추출
![슬라이드7](https://github.com/user-attachments/assets/7fd7b143-0212-4081-a52c-a12eaf25af2e)

Append는 concat을 랩핑한 메서드
unpack 배열과 batch 배열을 매 포문마다 합쳐서 새로 만들고 그걸 unpack에 할당하기 때문에 포문 도는 횟수만큼 배열 복사 작업이 일어나 메모리 누수 발생

아예 바로 concat을 사용하면 한번에 계산해서 딱 한번만 복사하므로 더 효율적
