import qrcode
import random

proverbs = [("가는 말이 고와야", "오늘 말이 곱다."), ("등잔 밑이", "어둡다."), ("개구리 올챙이", "적 생각 못한다."), ("티끌 모아" ,"태산"), ("벼는 익을수록", "고개를 숙인다."), ("원숭이도 나무에서", "떨어진다."), 
       ("낮말은 새가 듣고", "밤말은 쥐가 듣는다."), ("호랑이도", "제 말 하면 온다."), ("쇠뿔도", "단김에 빼라"), ("시작이", "반이다.")]
while True:
    a=random.choice(proverbs)
    print(a)
    img =qrcode.make(a)
    #img.save("qrcode.png")
    img.show()
    break

