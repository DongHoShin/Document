from pico2d import *


class Map:
    global stageNum
    global running
    def __init__(self):
        self.x = 0
        self.GrassX = 0
        self.GrassY = 0
        self.GrassZ = 0
        self.SetStage()

    def SetStage(self):
        if stageNum == 1:
            self.back = load_image('doublebackground.png')
            self.grass = load_image('ground1.png')
            self.GrassY = 50
            self.GrassZ = 100
        pass

    def update(self):
        if stageNum == 1:
            self.x = self.x - 5
            if self.x == -600:
               self.x = 600
            self.GrassX = (self.GrassX - 15)
            if self.GrassX == -600:
                self.GrassX = 600





    def draw(self):
        self.back.draw(self.x, 400, 1200, 800)
        self.back.draw(self.x+1200, 400, 1200, 800)
        self.grass.draw(self.GrassX, self.GrassY, 1200, self.GrassZ)
        self.grass.draw(self.GrassX+1200, self.GrassY, 1200, self.GrassZ)


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
        self.image.clip_draw(self.frame * 90, 0, 80, 90, 50, self.sY)


def handle_events():
    global lava
    global stageNum
    global running
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_DOWN:
                lava.state = lava.RUN
                lava.SetBoyImage()
            if event.key == SDLK_SPACE:
                lava.state = lava.RUN
                lava.SetBoyImage()

open_canvas(1200, 800)
stageNum = 1
stage = Map()
lava = Boy()
running = True


while running:
    handle_events()
    clear_canvas()
    stage.update()
    lava.update()

    stage.draw()

    lava.draw()
    update_canvas()
    delay(0.05)

close_canvas()


