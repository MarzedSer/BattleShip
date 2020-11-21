Desk= [[" |", "|1|", "|2|", "|3|", "|4|", "|5|", "|6|",],
       ["1|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["2|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["3|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["4|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["5|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["6|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"]]

class Desk:
    def __init__(self,T,z,zd):
        self.T=T
        self.z=z
        self.zd=zd
    def get_desk(self):
        return self.T,self.z,self.zd

class ship:
    def __init__(self,x,y,lenght,vg):
        self.x=x
        self.y=y
        self.lenght=lenght
        self.vg=vg
    def __str__(self):
        return self.x,self.y,self.lenght,self.vg


def draw():
    for x in Desk:
        print(x[0], x[1], x[2], x[3], x[4], x[5], x[6])

def step0():
    ship.x = int(input("Введите номер строки носа корабля = "))
    ship.y = int(input("Введите номер столбца носа кораблся = "))

    while  ship.x < 1 or  ship.x > 6 or ship.y < 1 or ship.y > 6:
        ship.x = int(input("Введите номер строки заного = "))
        ship.y = int(input("Введите номер столбца заного = "))

def step1():
    ship.lenght,ship.vg=int(input("Расположите корабли,введите какой корабль хотите расположить = ")),int(input("Если горизонтально,то введите 1,если вертикально,то 0 ="))

    if ship.lenght==3 and ship.vg==1:
        ship='■ ■ ■'
    if ship.lenght==3 and ship.vg==0:
        ship='■ \
              ■ \
              ■'
    if ship.lenght == 2 and ship.vg == 1:
        ship = '■ ■'
    if ship.lenght == 2 and ship.vg == 0:
        ship = '■ \
                ■'
    if ship.lenght == 1 and (ship.vg == 1 or ship.vg == 0) :
        ship = '■'

draw()
while True:
    step0()
    step1()

