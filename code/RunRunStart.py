import RunRun_Framework
import RunMain
from pico2d import*

name = "Start"
image = None
logo_time = 0.0

def enter():
    global image
    open_canvas(1200, 800)
    image = load_image("larva3.jpg")

def exit():
    global image
    del(image)
    close_canvas()

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            RunRun_Framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                RunRun_Framework.quit()

def update(frame_time):
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        RunRun_Framework.push_state(RunMain)

    logo_time += frame_time

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(600, 400, 1200, 800)
    update_canvas()