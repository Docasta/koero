from ursina import *
from random import randint
try:
    app = Ursina()
    kup = Entity(model='cube', color=color.red, scale=1)
    kop = Entity(model='sphere', color=color.white, scale=1)
    kop1 = Entity(model='cube', color=color.black, scale=1)
    kop2 = Entity(model='sphere', color=color.red, scale=1)
    def update():
        if held_keys["q"]:
            quit()
        if held_keys['w']:
            boy2 = randint(5, 50) / 10
            boy3 = randint(5, 50) / 10
            boy4 = randint(5, 50) / 10
            kup.scale = Vec3(boy2, boy3, boy4)
        if held_keys["r"]:
            kup.scale = 1
            kop.scale = 1
            kop1.scale = 1
            kop2.scale = 1
        if held_keys["c"]:
            b1 = float(input("Sayı gir: "))
            b2 = float(input("Sayı gir: "))
            b3 = float(input("Sayı gir: "))
            b4 = float(input("Sayı gir: "))
            kup.scale = b1
            kop.scale = b2
            kop1.scale = b3
            kop2.scale = b4
        if held_keys["b"]:
            boy2 = randint(5, 50) / 10
            boy3 = randint(5, 50) / 10
            boy4 = randint(5, 50) / 10
            boy22 = randint(5, 50) / 10
            boy23 = randint(5, 50) / 10
            boy24 = randint(5, 50) / 10
            boy222 = randint(5, 50) / 10
            boy223 = randint(5, 50) / 10
            boy224 = randint(5, 50) / 10
            boy2222 = randint(5, 50) / 10
            boy2223 = randint(5, 50) / 10
            boy2224 = randint(5, 50) / 10
            kup.scale = Vec3(boy2,boy3,boy4)
            kop.scale = Vec3(boy22,boy23,boy24)
            kop1.scale = Vec3(boy222,boy223,boy224)
            kop2.scale = Vec3(boy2222,boy2223,boy2224)
        if held_keys['s']:
            boy22 = randint(5, 50) / 10
            boy23 = randint(5, 50) / 10
            boy24 = randint(5, 50) / 10
            kop.scale = Vec3(boy22, boy23, boy24)
        if held_keys['d']:
            boy222 = randint(5, 50) / 10
            boy223 = randint(5, 50) / 10
            boy224 = randint(5, 50) / 10
            kop1.scale = Vec3(boy222, boy223, boy224)
        if held_keys['a']:
            boy2222 = randint(5, 50) / 10
            boy2223 = randint(5, 50) / 10
            boy2224 = randint(5, 50) / 10
            kop2.scale = Vec3(boy2222, boy2223, boy2224)
        if held_keys["m"]:
            kup.scale = 5
            kop.scale = 5
            kop1.scale = 5
            kop2.scale = 5
    app.run()
except:
    print("Hata oluştu:(")
