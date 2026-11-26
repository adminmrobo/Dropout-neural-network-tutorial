# 하루의 실험실 : 뉴런의 드롭아웃

**AHNBOAT LAB · 하루의 실험실 · EP.01**

실험조수 하루가 드롭아웃 실험을 직접 다시 돌리고, 숫자와 그림으로 설명합니다.

- 페이지: https://adminmrobo.github.io/Dropout-neural-network-tutorial/
- 연구실 홈: https://www.ahnboat.xyz/

## 무엇을 하나

학습할 때 은닉 뉴런마다 동전을 던져 약 절반을 끄고(p = 0.5), 살아남은 뉴런에는 2를 곱합니다(역 드롭아웃). 학습이 끝나면 모두 켭니다.

같은 1-64-1 tanh 망을 잡음 섞인 sin(3x) 점 12개로 두 번 학습시켰습니다. 한 번은 그냥, 한 번은 드롭아웃으로 학습했고, 학습은 경사하강법 60,000 스텝, 학습률 0.002입니다.

| | 일반 망 | 드롭아웃 망 |
|---|---:|---:|
| 새 점 99개 오차 (최종) | 0.135 | 0.045 |
| 새 점 오차 (100스텝) | 0.026 | 0.055 |
| 학습 점 오차 (최종) | 0.000 | 0.069 |
| 상위 8개 뉴런의 출력 가중치 몫 | 47 % | 33 % |

드롭아웃 망의 새 점 오차가 3배 작습니다. 대신 학습 점은 덜 외웁니다.

## 페이지 구성 (10개 파트, 대사 35개)

1. 인트로 · 2. 매 스텝 동전 던지기 · 3. 일반 망의 과적합 · 4. 이웃에 기댈 수 없다 · 5. 작은 시험들 · 6. 학습 후: 평균 · 7. Hinton et al., 2012 · 8. 코드: 마스크와 ×2 · 9. 결과: 3배 작은 오차 · 10. 정리

장면은 모두 캔버스로 그립니다. 작은 망 곡선과 평균 곡선은 학습이 끝난 가중치로 페이지 안에서 직접 계산합니다.

## 폴더

| 경로 | 내용 |
|---|---|
| `index.html` | 완성 페이지 (한 파일, 외부 요청 없음) |
| `data/dropout_run.json` | 실험 기록: 오차 곡선, 스냅숏 곡선 80개, 최종 가중치, 첫 60스텝 마스크 |
| `data/haru_lines.json` | 하루의 대사 (화면용) |
| `data/haru_sprites.json` | 하루 표정 7장 (WebP, 216px) |
| `tools/experiment.py` | 실험 재현 (numpy, 시드 51) |
| `tools/haru_sprites.py` | 캐릭터 팩에서 표정 그림 만들기 |
| `tools/build_page.py` | `page_template.html` + 데이터 → `index.html` |

다시 만들기 (저장소 맨 위 폴더에서):

```bash
python3 tools/experiment.py
python3 tools/haru_sprites.py   # ../fruitfly-lab-expressions 가 있을 때만
python3 tools/build_page.py
```

## 출처

- 실험 아이디어와 16줄 코드: “Machine Learning from Scratch, part 51: dropout” 릴. 원본 영상과 소리는 쓰지 않았고, 코드를 같은 시드로 다시 돌린 결과로 장면을 새로 그렸습니다.
- 드롭아웃 원 논문: Hinton et al., *Improving neural networks by preventing co-adaptation of feature detectors*, arXiv:1207.0580 (2012).
- 하루 그림: [fruitfly-lab-expressions](https://adminmrobo.github.io/fruitfly-lab-expressions/) 캐릭터 팩. 쓴 표정은 E07 설명, E01 기쁨, E08 안내, E04 놀람, E09 생각, E12 응원, E10 확인입니다.

Reon Ahn's Page © 2022 Reon Ahn · CC BY-NC 4.0
