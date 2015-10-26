import random
from pico2d import *
import os
os.chdir("C:\\2dgp\\image")



class Map:
    global stageNum
    def __init__(self):
        self.x = 0
        self.GrassX = 0
        self.GrassY = 0
        self.GrassZ = 0
        self.SetStage()

    def SetStage(self):
        if stageNum == 1:
            self.back = load_image('doublebackground.png')
            self.doublebackgrass = load_image('background2.2.png')
            self.grass = load_image('ground1.png')
            self.GrassY = 100
            self.GrassZ = 400
        # elif stageNum == 2:
        #     self.back = load_image('doublebackground10.2.png')
        #     self.doublebackgrass = load_image('bakground2.2.png')
        #     self.grass = load_image('ground1.1.png')
        #     self.GrassY = 600
        #     self.GrassZ = 1200
        # elif stageNum == 3:
        #     self.back = load_image('doublebackground10.3.png')
        #     self.doublebackgrass = load_image('background2.2.png')
        #     self.grass = load_image('ground1.2.png')
        #     self.GrassY = 600
        #     self.GrassZ = 1200
        # elif stageNum == 4:
        #     self.back = load_image('doublebackground10.4.png')
        #     self.doublebackgrass = load_image('background2.2.png')
        #     self.grass = load_image('ground1.3.png')
        #     self.GrassY = 500
        #     self.GrassZ = 1050

    def update(self):
          self.x = self.x - 10
          if self.x == -600:
               self.x = 600

          self.GrassX = (self.GrassX - 15)
          if self.GrassX == -600:
                self.GrassX = 600

    def draw(self):
        self.back.draw(self.x, 400, 1200, 800)
        self.back.draw(self.x+1200, 400, 1200, 800)
        self.doublebackgrass.draw(self.GrassX , 600, 1200, 670)
        self.doublebackgrass.draw(self.GrassX + 1200, 600, 1200, 670)
        self.grass.draw(self.GrassX, self.GrassY, 1200, self.GrassZ)
        self.grass.draw(self.GrassX+1200, self.GrassY, 1200, self.GrassZ)

class TrapRandom:
    global TrapList
    def __init__(self):
        self.x = 1500
    def SetStageTrap(self):
        for i in range(50):
            TrapList.append(Trap((i*500)+random.randint(-250,250)+1200, random.randint(1,3)))

    def updata(self):
        pass

class Trap:
    global stageNum
    def __init__(self, x, trapType):
        self.trapX = x
        self.trapY = 0
        self.frame = 0
        self.MaxFrame = 6
        self.type = trapType
        self.trap = load_image('1.1Trap.png')
        self.imageX = 0
        self.imageY = 0
        self.width = 0
        self.height = 0
        self.SetTrap()



    def SetTrap(self):
        if stageNum == 1:
            if self.type == 1:
                self.trap = load_image('1.1Trap.png')
                self.MaxFrame = 6
                self.imageX = 141
                self.imageY= 141
                self.trapY = 320
                self.width = 80
                self.height = 100
            elif self.type == 2:
                self.trap = load_image('1.3Trap.png')
                self.MaxFrame = 3
                self.imageX = 133
                self.imageY = 148
                self.trapY = 400
                self.width = 100
                self.height = 135
        # if stageNum == 2:
        #     if self.type == 1:
        #         self.trap = load_image('2.1Trap.png')
        #         self.MaxFrame = 12
        #         self.imageX = 142
        #         self.imageY= 58
        #         self.trapY = 180
        #         self.width = 130
        #         self.height = 100
        #     elif self.type == 2:
        #         self.trap = load_image('12.3Trap.png')
        #         self.MaxFrame = 16
        #         self.imageX = 173
        #         self.imageY = 136
        #         self.trapY = 400
        #         self.width = 200
        #         self.height = 135
        #
        # if stageNum == 3:
        #     if self.type == 1:
        #         self.trap = load_image('3.1Trap.png')
        #         self.MaxFrame = 6
        #         self.imageX = 97
        #         self.imageY= 149
        #         self.trapY = 180
        #         self.width = 130
        #         self.height = 100
        #     elif self.type == 2:
        #         self.trap = load_image('11.3Trap.png')
        #         self.MaxFrame = 6
        #         self.imageX = 97
        #         self.imageY = 149
        #         self.trapY = 400
        #         self.width = 200
        #         self.height = 400
        # if stageNum == 4:
        #     if self.type == 1:
        #         self.trap = load_image('4.1Trap.png')
        #         self.MaxFrame = 9
        #         self.imageX = 147
        #         self.imageY= 199
        #         self.trapY = 230
        #         self.width = 180
        #         self.height = 200
        #     elif self.type == 2:
        #         self.trap = load_image('10.3Trap.png')
        #         self.MaxFrame = 16
        #         self.imageX = 221
        #         self.imageY = 319
        #         self.trapY = 490
        #         self.width = 201
        #         self.height = 620
    def update(self):
        self.frame = (self.frame+1) % self.MaxFrame
        self.moving()
    def moving(self):
        self.trapX = (self.trapX-20)
    def draw(self):
        self.trap.clip_draw(self.frame * self.imageX, 0, self.imageX, self.imageY, self.trapX, self.trapY, self.width, self.height)

class Boy:

    RUN, SLIDING, JUMP = 0, 1, 2

    def __init__(self):
        self.sY = 135
        self.frame = 0
        self.image = load_image('YlarvaRun.png')
        self.speed = 0
        self.state = self.RUN

    def BoySpeed(self):
        if(self.sY-45-self.speed) > 90:
            self.speed += 3
            self.sY -= self.speed

        else:
            self.sY = 90+45
            self.speed = 0

    def SetBoyImage(self):
        self.frame = 0
        if self.state == 0:
            self.image = load_image('YlarvaRun.png')

        elif self.state == 1:
            self.image = load_image('YlarvaSlide.png')

        elif self.state == 2:
            self.image = load_image('YlarvaJump.png')


    def update(self):
        self.frame = (self.frame + 1) % 5
        self.BoySpeed()

    def draw(self):
        self.image.clip_draw(self.frame * 90, 0, 80, 90, 400, self.sY + 185)


def handle_events():
    global running
    global TitleSwitch
    global changeMap
    global lava
    global stageNum
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                if(lava.sY-45) == 90:
                    lava.speed = -25
                    lava.state = lava.JUMP
                lava.SetBoyImage()
            if event.key == SDLK_DOWN:
                lava.sY = 90 + 45
                lava.speed = 0
                lava.state = lava.SLIDING
                lava.SetBoyImage()
            elif event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_a:
                TitleSwitch = False
            elif event.key == SDLK_b:
                stageNum += 1
                if stageNum == 5:
                    stageNum = 1
                stage.SetStage()
                TrapList.clear()
                trapRandom.SetStageTrap()
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                lava.state = lava.RUN
                lava.SetBoyImage()
            if event.key == SDLK_SPACE:
                lava.state = lava.RUN
                lava.SetBoyImage()

open_canvas(1200, 800)
Title = load_image('larva3.jpg')
lava = Boy()
stageNum = 1
stage = Map()
TrapList = []
TitleSwitch = True
running = True
frame = 0
trapRandom = TrapRandom()
trapRandom.SetStageTrap()
show_cursor()
while (running):
    handle_events()
    clear_canvas()
    if TitleSwitch == False:
        for trap in TrapList:
            trap.update()
        stage.update()
        lava.update()

        stage.draw()
        lava.draw()
        for trap in TrapList:
            trap.draw()
    else:
        Title.draw(600, 400, 1200, 800)
    update_canvas()
    delay(0.06)

close_canvas()


