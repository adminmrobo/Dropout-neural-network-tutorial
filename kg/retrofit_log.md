# 개조 기록 — Dropout-neural-network-tutorial
- 날짜: 2026-11-28 · 도구: ai-lab-retrofit v1.8 (retrofit.py · check.py) · AI: Claude Opus 5.5
- 결과: 아래 check_report.md 참고 — 점검 오류 0, 본문 차이 0
- 꼬리표 원본: kg/pages/*.{kg,refs,meta}.json (하루의 실험실 대사·실험 기록·출처 칸에서 손으로 정리)
- anchor: 이 페이지는 한 화면 무대형(#stage)이라 모든 항목이 #stage를 가리킨다.

## 기본으로 붙는 방식
- tools/build_page.py가 페이지를 다시 만들면 끝에서 kg/reapply.py를 불러 지식 색인(#kg)·꾸러미(#export)를 다시 붙인다.
- 새 개념을 더하려면 kg/pages/의 kg.json을 고치고 python3 kg/reapply.py .

## 사람이 할 일
- 번역판을 만들 때는 이 한국어 원본의 kg-raw·page-meta를 언어팩으로 함께 옮긴다.
