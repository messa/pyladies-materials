import pyglet
from math import sin


WIDTH, HEIGHT = 640, 480
FROG_WIDTH, FROG_HEIGHT = 32, 32
FROG_STEP = 32

img_background = pyglet.image.load('images/pozadi.bmp')
img_frog_left = pyglet.image.load('images/frog1.bmp')
img_frog_right = pyglet.image.load('images/frog2.bmp')
img_frog_up = pyglet.image.load('images/frog3.bmp')
img_frog_down = pyglet.image.load('images/frog4.bmp')

background_sprite = pyglet.sprite.Sprite(img_background)


class Frog:

    def __init__(self):
        frog_img = img_frog_up.get_region(0, 0, FROG_WIDTH, FROG_HEIGHT)
        self.sprite = pyglet.sprite.Sprite(frog_img)
        self.sprite.x = WIDTH // 2
        self.sprite.y = 40

    def draw(self):
        self.sprite.draw()

    def go_left(self):
        self.sprite.x -= FROG_STEP

    def go_right(self):
        self.sprite.x += FROG_STEP

    def go_up(self):
        # souradnice Y=0 je spodni hrana, takze UP je pricitani Y
        self.sprite.y += FROG_STEP

    def go_down(self):
        # souradnice Y=0 je spodni hrana, takze DOWN je odcitani Y
        self.sprite.y -= FROG_STEP


frog = Frog()


window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


def tik(time_since_last_call):
    pass

pyglet.clock.schedule_interval(tik, 1/30)


def handle_draw():
    window.clear()
    background_sprite.draw()
    frog.draw()


def handle_text(text):
    for c in text.lower():
        if c == 'w':
            frog.go_up()
        elif c == 'a':
            frog.go_left()
        elif c == 's':
            frog.go_down()
        elif c == 'd':
            frog.go_right()
        elif c == 'q':
            print('Ukonceni klavesou Q')
            pyglet.app.exit()
        else:
            print('Neznama klavesa:', c)


window.push_handlers(
    on_draw=handle_draw,
    on_text=handle_text)

pyglet.app.run()