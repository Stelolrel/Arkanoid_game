import pygame
from random import*
from time import*
pygame.init()
window = pygame.display.set_mode((500,800))
window.fill((0,225,255))
clock = pygame.time.Clock()
shift_x=2
shift_y=2
hitbox=(255,0,0)
defaultC=(0,225,255)
class TextArea():
    def __init__(self,x=0,y=0,width=0,height=0,color=(0,225,255),outlinecolor=defaultC):
        self.rect = pygame.Rect(x,y,width,height)
        self.fill_outlinecolor = outlinecolor
        self.rect1 = pygame.Rect(x+2.5,y+2.5,width-5,height-5)
        self.fill_color = color  
    def fill(self):
        pygame.draw.rect(window,self.fill_color,self.rect)
    def set_text(self,text,fsize=0,text_color=None):
        self.text =(text)
        self.image = pygame.font.Font(None,fsize).render(text,True,text_color)
    def color(self,color=None,outlinecolor=None):
        self.fill_color = color
        self.fill_outlinecolor = outlinecolor
        
    def draw(self,shift_x=0,shift_y=0):
        pygame.draw.rect(window,self.fill_outlinecolor,self.rect)
        pygame.draw.rect(window,self.fill_color,self.rect1)
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))
    def collidepoint(self,rect1):
        return self.rect.colliderect(rect1)
class Picture(TextArea):
    def __init__(self,filename,x=0,y=0,width=0,height=0,size=(500,500),degree=0):
        super().__init__(x=x,y=y,width=width,height=height)
        image = pygame.image.load(filename)
        self.image = pygame.transform.scale(image, size)
        self.image = pygame.transform.rotate(self.image, degree)
    def imagedraw(self,shift_x,shift_y):
        pygame.draw.rect(window,self.fill_outlinecolor,self.rect)
        pygame.draw.rect(window,self.fill_color,self.rect1)
        window.blit(self.image, (self.rect.x + shift_x,self.rect.y + shift_y))
booster1=Picture('speed.png',x=2400,y=600,width=50,height=50,size=(40,40))
booster1.imagedraw(shift_x,shift_y)

booster2=Picture('plus.png',x=2200,y=600,width=50,height=50,size=(40,40))
booster2.imagedraw(shift_x,shift_y)

booster3=Picture('minus.png',x=2300,y=600,width=50,height=50,size=(40,40))
booster3.imagedraw(shift_x,shift_y)

booster4=Picture('slow.png',x=2100,y=600,width=50,height=50,size=(40,40))
booster4.imagedraw(shift_x,shift_y)

booster5=Picture('2ball.png',x=2220,y=600,width=50,height=50,size=(40,40))
booster5.imagedraw(shift_x,shift_y)

booster6=Picture('shield.png',x=2100,y=550,width=50,height=50,size=(40,40))
booster6.imagedraw(shift_x,shift_y)
shields=[]

x=10
enemy=[]
for i in range(9):
    new_enemy=Picture('enemy.png',x,y=100,width=42,height=40,size=(40,40))
    new_enemy.imagedraw(shift_x,shift_y)
    enemy.append(new_enemy)
    x+=55
x=35
for i in range(8):
    new_enemy=Picture('enemy.png',x,y=150,width=42,height=40,size=(40,40))
    new_enemy.imagedraw(shift_x,shift_y)
    enemy.append(new_enemy)
    x+=55
x=60
for i in range(7):
    new_enemy=Picture('enemy.png',x,y=200,width=42,height=40,size=(40,40))
    new_enemy.imagedraw(shift_x,shift_y)
    enemy.append(new_enemy)
    x+=55
x=0

ball=Picture('ball.png',x=100,y=350,width=55,height=55,size=(40,40))
ball.imagedraw(shift_x+5,shift_y+5)

ball2=Picture('ball.png',x=10000,y=350,width=55,height=55,size=(40,40))
ball2.imagedraw(shift_x+5,shift_y+5)

stick=Picture('platform.png',x=10,y=510,width=112,height=26,size=(90,26))
stick.imagedraw(shift_x+5,shift_y)

wall3 = TextArea(x=0,y=0,width=500,height=105,color=defaultC,outlinecolor=defaultC)
wall3.set_text('',0,(0,0,0))
wall3.draw(shift_x,shift_y)

chenar1 = TextArea(x=100,y=0,width=300,height=100,color=(255,0,0),outlinecolor=(0,0,0))
chenar1.set_text('Shop at Aldi game',40,(0,0,0))
chenar1.draw(shift_x=15,shift_y=35)

wall1 = TextArea(x=490,y=0,width=50,height=800,color=defaultC,outlinecolor=defaultC)
wall1.set_text('',0,(0,0,0))
wall1.draw(shift_x,shift_y)

wall2 = TextArea(x=-40,y=0,width=45,height=800,color=defaultC,outlinecolor=defaultC)
wall2.set_text('',0,(0,0,0))
wall2.draw(shift_x,shift_y)

wall4 = TextArea(x=0,y=700,width=500,height=105,color=defaultC,outlinecolor=defaultC)
wall4.set_text('',0,(0,0,0))
wall4.draw(shift_x,shift_y)

speedX= 2
speedY = 2
speedX2= 2
speedY2 = 2
timerS=0
win_condition=0
result = 'press q to start'
resultS = TextArea(x=100,y=350,width=300,height=100,color=(255,255,255),outlinecolor=(0,0,0))
resultS.set_text(result,30,(0,0,0))
resultS.draw(shift_x=15,shift_y=35,)
resultS.color(defaultC,defaultC)
value=1
while value ==1:
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    value=2
resultS.set_text('',30,(0,0,0))
resultS.color(defaultC,defaultC)
resultS.draw(shift_x=15,shift_y=35,)
Move_Left=False
Move_Right=False
Rbooster=0
Sspeed=3
BCvalue =1
wait=0
Ivalue=0
while win_condition==0:
    chenar1.draw(shift_x=15,shift_y=35)
    Rvalue = randint(1,30)
    pygame.display.update()
    clock.tick(48)
    if Rvalue == 1:
        if BCvalue ==1:
            Rbooster = randint(0,6)
            Ivalue=1
            BCvalue=0
    if Rbooster == 1:
        if Ivalue ==1:
            booster1.rect.x=randint(50,450)
            booster1.rect1.x=booster1.rect.x
            booster1.rect.y=210
            booster1.rect1.y=210
            Ivalue=0
            wait = 500
        booster1.rect.y+=3
        booster1.rect1.y+=3
        booster1.imagedraw(2,2)
        if timerS ==1:
            wait-=1
            if wait <= 0:
                    Sspeed=3
                    BCvalue=1
                    timerS=0
        if booster1.collidepoint(stick.rect):
            timerS=1
            booster1.rect.x=2000
            booster1.rect1.x=booster1.rect.x
            booster1.rect.y=110
            booster1.rect1.y=110
            booster1.imagedraw(2,2)
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
            Sspeed=7
        if booster1.collidepoint(wall4.rect):
            timerS=1
            booster1.rect.x=2350
            booster1.rect1.x+=booster1.rect.x
            booster1.rect.y=750
            booster1.rect1.y=750
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
            BCvalue=1
            timerS=0
            wait=0
            
            

    elif Rbooster == 2:
        if Ivalue ==1:
            booster2.rect.x=randint(50,450)
            booster2.rect1.x=booster2.rect.x
            booster2.rect.y=210
            booster2.rect1.y=210
            Ivalue=0
            wait = 500
        booster2.rect.y+=3
        booster2.rect1.y+=3
        booster2.imagedraw(2,2)
        if timerS ==1:
            wait-=1
            if wait <= 0:
                    stick.rect.x+=2000
                    stick.rect1.x+=2000
                    stick=Picture('platform.png',x=250,y=510,width=112,height=26,size=(90,25))
                    stick.imagedraw(shift_x+5,shift_y)
                    window.fill((0,225,255))
                    stick.imagedraw(shift_x+5,shift_y)
                    BCvalue=1
                    timerS=0
        if booster2.collidepoint(stick.rect):
            timerS=1
            booster2.rect.x=2000
            booster2.rect1.x=booster2.rect.x
            booster2.rect.y=110
            booster2.rect1.y=110
            booster2.imagedraw(2,2)
            stick.rect.x=2000
            stick.rect1.x=2000
            stick=Picture('platform.png',x=250,y=510,width=168,height=39,size=(120,38))
            stick.imagedraw(shift_x+5,shift_y)
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
        if booster2.collidepoint(wall4.rect):
            timerS=1
            booster2.rect.x=2350
            booster2.rect1.x+=booster2.rect.x
            booster2.rect.y=750
            booster2.rect1.y=750
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
            BCvalue=1
            timerS=0
            wait=0
            
                
        

    elif Rbooster == 3:
        if Ivalue ==1:
            booster3.rect.x=randint(50,450)
            booster3.rect1.x=booster3.rect.x
            booster3.rect.y=210
            booster3.rect1.y=210
            Ivalue=0
            wait = 500
        booster3.rect.y+=3
        booster3.rect1.y+=3
        booster3.imagedraw(2,2)
        if timerS ==1:
            wait-=1
            if wait <= 0:
                    stick.rect.x=2000
                    stick.rect1.x=2000
                    stick.imagedraw(shift_x+5,shift_y)
                    stick=Picture('platform.png',x=250,y=510,width=112,height=26,size=(90,25))
                    stick.imagedraw(shift_x+5,shift_y)
                    BCvalue=1
                    window.fill((0,225,255))
                    stick.imagedraw(shift_x+5,shift_y)
                    timerS=0
        if booster3.collidepoint(stick.rect):
            timerS=1
            booster3.rect.x=2000
            booster3.rect1.x=booster3.rect.x
            booster3.rect.y=110
            booster3.rect1.y=110
            booster3.imagedraw(2,2)
            stick.rect.x=2000
            stick.rect1.x=2000
            stick.imagedraw(shift_x+5,shift_y)
            stick=Picture('platform.png',x=250,y=510,width=62,height=15,size=(45,12))
            stick.imagedraw(shift_x+5,shift_y)
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
        if booster3.collidepoint(wall4.rect):
            timerS=1
            booster3.rect.x=2350
            booster3.rect1.x+=booster3.rect.x
            booster3.rect.y=750
            booster3.rect1.y=750
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
            BCvalue=1
            timerS=0
            wait=0
            

    elif Rbooster == 4:
        if Ivalue ==1:
            booster4.rect.x=randint(50,450)
            booster4.rect1.x=booster4.rect.x
            booster4.rect.y=210
            booster4.rect1.y=210
            booster4.imagedraw(2,2)
            Ivalue=0
            wait=500
        booster4.rect.y+=3
        booster4.rect1.y+=3
        booster4.imagedraw(2,2)
        if timerS ==1:
            wait-=1
            if wait <= 0:
                Sspeed=3
                BCvalue=1
                timerS=0
        if booster4.collidepoint(stick.rect):
            timerS=1
            booster4.rect.x=2350
            booster4.rect1.x+=booster4.rect.x
            booster4.rect.y=750
            booster4.rect1.y=750
            Sspeed=1
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
        if booster4.collidepoint(wall4.rect):
            timerS=1
            booster4.rect.x=2350
            booster4.rect1.x+=booster4.rect.x
            booster4.rect.y=750
            booster4.rect1.y=750
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
            BCvalue=1
            timerS=0
            wait=0

            

    elif Rbooster == 5:
        if Ivalue ==1:
            booster5.rect.x=randint(50,450)
            booster5.rect1.x=booster5.rect.x
            booster5.rect.y=210
            booster5.rect1.y=210
            Ivalue=0
            wait = 700
        booster5.rect.y+=3
        booster5.rect1.y+=3
        booster5.imagedraw(2,2)
        if timerS ==1:
            wait-=1
            if wait <= 0:
                    ball2.rect.x+=2000
                    ball2.rect1.x+=2000
                    ball2.imagedraw(shift_x+5,shift_y)
                    window.fill((0,225,255))
                    stick.imagedraw(shift_x+5,shift_y)
                    BCvalue=1
                    timerS=0
        if booster5.collidepoint(stick.rect):
            timerS=1
            booster5.rect.x=2000
            booster5.rect1.x=booster5.rect.x
            booster5.rect.y=110
            booster5.rect1.y=110
            booster5.imagedraw(2,2)
            ball2.rect.x=50
            ball2.rect1.x=50
            ball2.rect.y=400
            ball2.rect1.y=400
            stick.imagedraw(shift_x+5,shift_y)
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
        if booster5.collidepoint(wall4.rect):
            timerS=1
            booster5.rect.x=2350
            booster5.rect1.x+=booster2.rect.x
            booster5.rect.y=750
            booster5.rect1.y=750
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
            BCvalue=1
            timerS=0
            wait=0

    elif Rbooster == 6:
        if Ivalue ==1:
            booster6.rect.x=randint(50,450)
            booster6.rect1.x=booster6.rect.x
            booster6.rect.y=210
            booster6.rect1.y=210
            Ivalue=0
        booster6.rect.y+=3
        booster6.rect1.y+=3
        booster6.imagedraw(2,2)
        if booster6.collidepoint(stick.rect):
            BCvalue=1
            booster6.rect.x=2350
            booster6.rect1.x+=booster4.rect.x
            booster6.rect.y=750
            booster6.rect1.y=750
            shields.clear()
            x=50
            for i in range(3):
                Bshield= TextArea(x,y=475,width=100,height=10,color=(0,0,255),outlinecolor=(0,0,0))
                Bshield.set_text('',40,(0,0,0))
                Bshield.draw(shift_x=15,shift_y=35)
                shields.append(Bshield)
                x+=150
            x=0
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
            BCvalue=1
        if booster6.collidepoint(wall4.rect):
            BCvalue=1
            booster6.rect.x=2350
            booster6.rect1.x+=booster4.rect.x
            booster6.rect.y=750
            booster6.rect1.y=750
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)

    print(Rbooster)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Move_Right=True
            if event.key == pygame.K_d:
                Move_Left=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Move_Right=False
            if event.key == pygame.K_d:
                Move_Left=False 
    if Move_Right == True:
        stick.rect.x =stick.rect.x - Sspeed
        stick.rect1.x =stick.rect1.x -Sspeed
        stick.imagedraw(shift_x+5,shift_y)
    if Move_Left == True:
        stick.rect.x =stick.rect.x + Sspeed
        stick.rect1.x =stick.rect1.x + Sspeed
        stick.imagedraw(shift_x+5,shift_y)
    for new_enemy in enemy:
        new_enemy.draw(shift_x,shift_y)
        if new_enemy.rect.colliderect(ball.rect) :
            new_enemy.fill()
            speedY *= -1
            enemy.remove(new_enemy)
        if new_enemy.rect.colliderect(ball2.rect) :
            new_enemy.fill()
            speedY2 *= -1
            enemy.remove(new_enemy)
        else:
            sleep(0)
    for Bshield in shields:
        Bshield.draw(shift_x,shift_y)
        if Bshield.rect.colliderect(ball.rect) :
            Bshield.fill()
            speedY *= -1
            shields.remove(Bshield)
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
        if Bshield.rect.colliderect(ball2.rect) :
            Bshield.fill()
            speedY *= -1
            shields.remove(Bshield)
            window.fill((0,225,255))
            stick.imagedraw(shift_x+5,shift_y)
        else:
            sleep(0)
        sleep(0)
    if stick.collidepoint(wall1.rect) :
        stick.rect.x =stick.rect.x - Sspeed
        stick.rect1.x =stick.rect1.x - Sspeed
    else:
        sleep(0)
    if stick.collidepoint(wall2.rect) :
        stick.rect.x =stick.rect.x + Sspeed
        stick.rect1.x =stick.rect1.x + Sspeed
    else:
        sleep(0)
    if len(enemy) ==0:
        win_condition=1
    Bvalue = 1
    while Bvalue ==1:
        ball.rect.x += speedX
        ball.rect1.x +=speedX
        ball.rect.y +=speedY
        ball.rect1.y +=speedY
        ball.imagedraw(shift_x+5,shift_y+5)
        if ball.collidepoint(ball2.rect) :
            speedY *= -1
            speedX *= -1
        if ball.collidepoint(wall3.rect) :
            speedY *= -1  
        else:
            sleep(0)
        if ball.collidepoint(wall4.rect) :
            win_condition=-1
        else:
            sleep(0)
        if ball.collidepoint(stick.rect1) :
            speedY *= -1 
        if ball.collidepoint(wall1.rect) :
            speedX *= -1  
        else:
            sleep(0)
        if ball.collidepoint(wall2.rect) :
            speedX *= -1  
        Bvalue=0
    Bvalue = 1
    while Bvalue ==1:
        ball2.rect.x += speedX2
        ball2.rect1.x +=speedX2
        ball2.rect.y +=speedY2
        ball2.rect1.y +=speedY2
        ball2.imagedraw(shift_x+5,shift_y+5)
        if ball2.collidepoint(ball.rect) :
            speedY2 *= -1
            speedX2 *= -1
        if ball2.collidepoint(wall3.rect) :
            speedY2 *= -1  
        else:
            sleep(0)
        if ball2.collidepoint(wall4.rect) :
            win_condition=-1
        else:
            sleep(0)
        if ball2.collidepoint(stick.rect1) :
            speedY2 *= -1 
        if ball2.collidepoint(wall1.rect) :
            speedX2 *= -1  
        else:
            sleep(0)
        if ball2.collidepoint(wall2.rect) :
            speedX2 *= -1  
        Bvalue=0
    print(Rvalue)
    print(Rbooster)
    result= 'booster time:'+str(wait/100)
    if wait > -1:
        resultS = TextArea(x=0,y=700,width=500,height=100,color=(255,255,255),outlinecolor=(0,0,0))
        resultS.set_text(result,40,(0,0,0))
        resultS.draw(shift_x=15,shift_y=15)

value=1
while value ==1:
    pygame.display.update()
    clock.tick(48)
    if win_condition == -1:
        chenar1 = TextArea(x=100,y=300,width=300,height=100,color=hitbox,outlinecolor=(0,0,0))
        chenar1.set_text('You Lost',70,(0,0,0))
        chenar1.draw(shift_x=15,shift_y=35)
    elif win_condition== 1:
        chenar1 = TextArea(x=0,y=250,width=500,height=200,color=(0,255,0),outlinecolor=(0,0,0))
        chenar1.set_text('You Win',140,(0,0,0))
        chenar1.draw(shift_x=15,shift_y=35)
    else:
        sleep(0)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                value=2
     

