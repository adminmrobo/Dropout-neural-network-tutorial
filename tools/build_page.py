"""index.html 만들기 — tools/page_template.html 에 실험 데이터·대사·하루 그림을 넣는다.

순서
  1) python3 tools/experiment.py      # data/dropout_run.json (같은 시드 51로 다시 실행)
  2) python3 tools/haru_sprites.py    # 캐릭터 팩에서 하루 표정 7장 → data/haru_sprites.json
  3) python3 tools/build_page.py      # index.html
저장소 맨 위 폴더에서 실행한다.
"""
import json

s = open("tools/page_template.html", encoding="utf-8").read()
s = s.replace("__HARU__", open("data/haru_sprites.json", encoding="utf-8").read())
s = s.replace("__DATA__", open("data/dropout_run.json", encoding="utf-8").read())
lines = json.load(open("data/haru_lines.json", encoding="utf-8"))
s = s.replace("__SCRIPT__", json.dumps(lines, ensure_ascii=False, separators=(",", ":")))
open("index.html", "w", encoding="utf-8").write(s)
print("index.html", len(s.encode()), "bytes")
