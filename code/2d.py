from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('ground1.png')

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(800, 30)


class BackImage:
    def __init__(self):
        self.image = load_image('doublebackground.png')

    def draw(self):
        self.image.draw(500, 450)
        self.image.draw(1530, 450)


class Boy:

    RUN, SLIDING, JUMP = 0, 1, 2

    def __init__(self):
        self.sY = 115
        self.frame = 0
        self.image = load_image('YlarvaRun.png')
        self.speed = 0
        self.state = self.RUN
        self.MaxFrame = 5

    def BoySpeed(self):
        if(self.sY-45-self.speed) > 70:
            self.speed += 3
            self.sY -= self.speed
        else:
            self.sY = 70+45
            self.speed = 0

    def SetBoyImage(self):
        self.frame = 0
        if self.state == 0:
            self.image = load_image('YlarvaRun.png')
            MaxFrame = 4
        elif self.state == 1:
            self.image = load_image('YlarvaSlide.png')
            MaxFrame = 4
        elif self.state == 2:
            self.image = load_image('YlarvaJump.png')
            MaxFrame = 4

    def update(self):
        self.frame = (self.frame + 1) % self.MaxFrame
        self.BoySpeed()

    def draw(self):
        self.image.clip_draw(self.frame * 90, 0, 90, 90, 50, self.sY)


def handle_events():
    global lava
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                if(lava.sY-45) == 70:
                    lava.speed = -25
                    lava.state = lava.JUMP
                lava.SetBoyImage()
            if event.key == SDLK_DOWN:
                lava.sY = 70 + 45
                lava.speed = 0
                lava.state = lava.SLIDING
                lava.SetBoyImage()
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDLK_SPACE:
            if event.key == SDLK_DOWN:
                lava.state = lava.RUN
                lava.SetBoyImage()
            if event.key == SDLK_UP:
                lava.state = lava.RUN
                lava.SetBoyImage()

open_canvas(1200, 800)

lava = Boy()
grass = Grass()
back = BackImage()
running = True


while running:
    handle_events()

    lava.update()

    clear_canvas()
    back.draw()
    grass.draw()

    lava.draw()
    update_canvas()
    delay(0.05)

close_canvas()


