import random
import RunRun_Framework
from pico2d import*

lava = None
stage = None
trapRandom = None
frame = 0
stageNum = 1
TrapList = []

class Map:
    global stageNum, lava
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
    global TrapList, stageNum
    def __init__(self):
        self.x = 1500
    def SetStageTrap(self):
        for i in range(30):
            if stageNum == 1:
                TrapList.append(Trap((i*750)+random.randint(-250,250)+1200, random.randint(1,3)))
            if stageNum == 2:
                TrapList.append(Trap((i*750)+random.randint(-250,250)+1200, random.randint(1,3)))
            if stageNum == 3:
                TrapList.append(Trap(((-i)*750)+random.randint(-250,250)-1200, random.randint(1,3)))
            if stageNum == 4:
                TrapList.append(Trap(((-i)*750)+random.randint(-250,250)+1200, random.randint(1,3)))
    def updata(self):
        pass


class Trap:
    global stageNum
    global lava
    global TrapList

    def __init__(self, x, trapType):
        self.trapX = x
        self.trapY = 0
        self.frame = 0
        self.MaxFrame = 6
        self.type = trapType
        self.trap = None
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

    def hit(self):
        for i in range(30):
            if stageNum == 1:
                if (lava.yellowX+lava.width/3) >= (TrapList[i].trapX - TrapList[i].width/4) and (lava.yellowX-lava.width/3) <= (TrapList[i].trapX + TrapList[i].width/4):
                    if TrapList[i].type == 1 and (lava.yellowY - lava.height/3) <= (TrapList[i].trapY + TrapList[i].height/3) and (lava.yellowY + lava.height/3) >= (TrapList[i].trapY - TrapList[i].height/3):
                        return True
                    if TrapList[i].type == 2 and (lava.yellowY - lava.height/3) <= (TrapList[i].trapY + TrapList[i].height/3) and (lava.yellowY + lava.height/3) >= (TrapList[i].trapY - TrapList[i].height/3):
                        return True
                    if TrapList[i].type == 3 and (lava.yellowY - lava.height/2) <= (TrapList[i].trapY + TrapList[i].height/2) and (lava.yellowY + lava.height/2) >= (TrapList[i].trapY - TrapList[i].height/2):
                        return True

        return False


    def update(self):
        self.frame = (self.frame+1) % self.MaxFrame
        self.moving()
    def moving(self):
        self.trapX = (self.trapX-20)

        if self.hit() == True:
            lava.SetCharacter(lava.BUMP)


    def draw(self):
        self.trap.clip_draw(self.frame * self.imageX, 0, self.imageX, self.imageY, self.trapX, self.trapY, self.width, self.height)


class Boy:
    RUN, SLIDING, JUMP, BUMP = 0, 1, 2, 3
    def __init__(self):
        self.sY = 135
        self.frame = 0
        self.image = load_image('YlarvaRun.png')
        self.speed = 0
        self.state = self.RUN
        self.MaxFrame = 5
        self.width = 90
        self.height = 90
        self.heightJumpRun = 90
        self.heightSlide = 70
        self.lastAnimateTime = get_time()
        self.buffList = []
        self.jumpNum = 0

    def BoySpeed(self):
        if(self.sY-45-self.speed) > 90:
            self.speed += 3
            self.sY -= self.speed

        else:
            self.sY = 90+45
            self.speed = 0

    def SetBoyImage(self, state):
        if state != self.state:
            if self.state == 0:
                self.image = load_image('YlarvaRun.png')

            elif self.state == 1:
                self.image = load_image('YlarvaSlide.png')

            elif self.state == 2:
                self.image = load_image('YlarvaJump.png')

            elif self.state == 3:
                self.image = load_image('YlarvaBump.png')


    def update(self):
        self.frame = (self.frame + 1) % 5
        self.BoySpeed()

    def draw(self):
        self.image.clip_draw(self.frame * 90, 0, 80, 90, 400, self.sY + 185)



def enter():
    global lava, stage, trapRandom, stageNum, frame, TrapList
    stage = Map()
    stage.SetStage()
    lava = Boy()
    trapRandom = TrapRandom()
    trapRandom.SetStageTrap()
    show_cursor()
    frame = 0
    stageNum = 1

def exit():
    global lava, stage, trapRandom, trap
    del(stage)
    del(lava)
    del(trapRandom)
    for trap in TrapList:
        del(trap)

def resume():
    global stage, stageNum
    stageNum = 1
    stage.bkframe = 0
    stage.doubleX = 600
    stage.doubleY = 400
    stage.grassX = 0
    stage.grassY = 0
    stage.grassZ = 0
    stage.SetStage()


def handle_events(self):
    global lava
    global stageNum
    global stage

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            RunRun_Framework.quit()
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
            RunRun_Framework.quit()
        elif event.key == SDLK_b:
            stageNum += 1
            if stageNum == 5:
                stageNum = 1







