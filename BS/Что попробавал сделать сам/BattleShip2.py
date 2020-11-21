desk= [["||", "|1|", "|2|", "|3|", "|4|", "|5|", "|6|",],
       ["1|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["2|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["3|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["4|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["5|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"],
       ["6|", "|o|", "|o|", "|o|", "|o|", "|o|", "|o|"]]

def draw():
    for ship in desk:
        print(ship[0], ship[1], ship[2], ship[3],ship[4], ship[5], ship[6])

class ship:
    def __init__(self,x,y,length ):
        self.x = x
        self.y = y
        self.lenght = lenght
    def get_ship(self):
        return self.x,self.y,self.lenght

def step():
        i=int(input("Введите кол-во палуб корабля="))
        x=int(input("Введите строку носа кораблся="))
        y=int(input("Введите ряд носа кораблся="))
        vg = int(input("Введите 0,если вертикально и 1.если горизантально="))

        while x < 1 or x > 6 or y < 1 or y > 6 or i < 1 or i > 3 or desk[x][y]=='|■|' or desk[x+1][y]=='|■|' or desk[x][y+1]=='|■|'or desk[x-1][y]=='|■|' or desk[x][y-1]=='|■|' or desk[x+1][y+1]=='|■|' or desk[x-1][y-1]=='|■|':
            i = int(input("Введите кол-во палуб корабля заного="))
            x = int(input("Введите строку носа кораблся заного="))
            y = int(input("Введите ряд носа кораблся заного="))
            vg = int(input("Введите 0,если вертикально и 1.если горизантально="))
        if i==1 and vg==0:
            ship=desk[x][y]='|■|'
        if i==2 and vg==0:
            while x>=6:
                i = int(input("Введите кол-во палуб корабля заного="))
                x = int(input("Введите строку носа кораблся заного="))
                y = int(input("Введите ряд носа кораблся заного="))
                vg = int(input("Введите 0,если вертикально и 1.если горизантально="))
            ship=desk[x][y]='|■|'
            ship=desk[x+1][y]='|■|'
        if i==3 and vg==0:
            while x>=5:
                i = int(input("Введите кол-во палуб корабля заного="))
                x = int(input("Введите строку носа кораблся заного="))
                y = int(input("Введите ряд носа кораблся заного="))
                vg = int(input("Введите 0,если вертикально и 1.если горизантально="))
            ship=desk[x][y]='|■|'
            ship=desk[x+1][y]='|■|'
            ship=desk[x+2][y] ='|■|'

        if i==1 and vg==1:
            ship=desk[x][y]='|■|'
        if i==2 and vg==1:
            while y>=6:
                i = int(input("Введите кол-во палуб корабля заного="))
                x = int(input("Введите строку носа кораблся заного="))
                y = int(input("Введите ряд носа кораблся заного="))
                vg = int(input("Введите 0,если вертикально и 1.если горизантально="))
            ship=desk[x][y]='|■|'
            ship=desk[x][y+1]='|■|'
        if i==3 and vg==1:
            while y>=5:
                i = int(input("Введите кол-во палуб корабля заного="))
                x = int(input("Введите строку носа кораблся заного="))
                y = int(input("Введите ряд носа кораблся заного="))
                vg = int(input("Введите 0,если вертикально и 1.если горизантально="))
            ship=desk[x][y]='|■|'
            ship=desk[x][y+1]='|■|'
            ship=desk[x][y+2] ='|■|'

while True:
    draw()
    step()