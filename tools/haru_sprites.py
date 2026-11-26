from PIL import Image
import base64, io, json
# 캐릭터 팩 저장소(adminmrobo/fruitfly-lab-expressions, f114fd2판)를 옆 폴더에 받아 둔다
SRC="../fruitfly-lab-expressions/images/haru/"
M={"neutral":"E07_explaining","happy":"E01_joy","point":"E08_guiding","surprise":"E04_surprise","think":"E09_thinking","cheer":"E12_cheering","wink":"E10_confirming"}
out={};tot=0
for k,f in M.items():
    im=Image.open(SRC+f+".png").convert("RGB"); w,h=im.size
    img=im.resize((216,216),Image.LANCZOS)
    b=io.BytesIO(); img.save(b,"WEBP",quality=86,method=6); out[k]="data:image/webp;base64,"+base64.b64encode(b.getvalue()).decode(); tot+=len(b.getvalue())
json.dump(out,open("data/haru_sprites.json","w")); print(tot)
