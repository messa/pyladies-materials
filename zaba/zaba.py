import pyglet
from random import choice, random, randrange
from math import sin


# pár konstant na začátek - rozměry okna, žáby, aut

WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
FROG_WIDTH, FROG_HEIGHT = 32, 32
CAR_WIDTH, CAR_HEIGHT = 32, 32
MIN_GAP = 10 # minimální mezera mezi dvěma auty

START_LINE_Y = 40
FINISH_LINE_Y = 424

LANES_Y = [72, 104, 136, 200, 232, 264, 328, 360, 392]


# načteme obrázky

img_background = pyglet.image.load('images/pozadi.bmp')
#img_frog_left = pyglet.image.load('images/frog1.bmp')
#img_frog_right = pyglet.image.load('images/frog2.bmp')
img_frog_up = pyglet.image.load('images/frog3.bmp')
#img_frog_down = pyglet.image.load('images/frog4.bmp')

# v img_frog_up jsou celkem 4 "podobrázky", ze kterých se dá zřejmě složit
# animace, ale to zatím nebudeme řešit a prostě vezmeme ten první podobrázek
frog_img = img_frog_up.get_region(0, 0, FROG_WIDTH, FROG_HEIGHT)



# Vysvětlivky:
# RTL = right to left = zprava doleva
# LTR = left to right = zleva doprava

img_cars_rtl = [pyglet.image.load(f'images/{i}.bmp') for i in range(1, 13, 2)]
img_cars_ltr = [pyglet.image.load(f'images/{i}.bmp') for i in range(2, 13, 2)]


# připravíme si pomocnou funkci


def sprites_overlap(sprite1, sprite2, gap=0):
    '''
    Vrátí True, pokud se dva sprite překrývají nebo je mezi nimi mezera menší než gap.
    '''
    if sprite1.y != sprite2.y:
        # jsou v úplně jiných jízdních pruzích
        return False
    if sprite1.x + sprite1.width + gap <= sprite2.x:
        # sprite1 je nalevo od sprite2, nepřekrývají se
        return False
    if sprite2.x + sprite2.width + gap <= sprite1.x:
        # sprite2 je nalevo od sprite1, nepřekrývají se
        return False
    # sprites se překrývají
    return True


# a jdeme na business logiku :)


class Frog:

    def __init__(self):
        self.sprite = pyglet.sprite.Sprite(frog_img)
        # nastavíme výchozí pozici žáby:
        self.sprite.x = WINDOW_WIDTH // 2
        self.sprite.y = START_LINE_Y
        self.remaining_lives = 3

    def draw(self):
        # voláno z handle_draw
        self.sprite.draw()

    def go_left(self):
        self.sprite.x = max(self.sprite.x - FROG_WIDTH, 0)

    def go_right(self):
        self.sprite.x = min(self.sprite.x + FROG_WIDTH, WINDOW_WIDTH)

    def go_up(self):
        # souradnice Y=0 je spodni hrana, takze UP je pricitani Y
        self.sprite.y = min(self.sprite.y + FROG_HEIGHT, FINISH_LINE_Y)
        if self.sprite.y == FINISH_LINE_Y:
            print('Finish!!!')

    def go_down(self):
        # souradnice Y=0 je spodni hrana, takze DOWN je odcitani Y
        self.sprite.y = max(self.sprite.y - FROG_HEIGHT, START_LINE_Y)

    def killed(self):
        self.sprite.x = WINDOW_WIDTH // 2
        self.sprite.y = START_LINE_Y
        self.remaining_lives -= 1

    def finish_reached(self):
        return self.sprite.y == FINISH_LINE_Y



class Car:

    def __init__(self, x, y, speed):
        self.speed = speed
        self.sprite = pyglet.sprite.Sprite(self.get_random_image())
        self.sprite.x = x
        self.sprite.y = y

    def get_random_image(self):
        if self.speed > 0:
            # vybereme obrázek auta ve směru zleva doprava
            return choice(img_cars_ltr)
        else:
            # vybereme obrázek auta ve směru zprava doleva
            return choice(img_cars_rtl)

    def draw(self):
        self.sprite.draw()

    def tick(self, time_since_last_call):
        self.sprite.x = self.sprite.x + self.speed * time_since_last_call

        if self.sprite.x < - CAR_WIDTH:
            # auto zmizelo vlevo - vrátíme ho zprava
            self.sprite.x = WINDOW_WIDTH
            # nastavíme jiný obrázek
            self.sprite.image = self.get_random_image()

        if self.sprite.x > WINDOW_WIDTH:
            # auto zmizelo vpravo - vrátíme ho zleva
            self.sprite.x = - CAR_WIDTH
            # nastavíme jiný obrázek
            self.sprite.image = self.get_random_image()


# vytvoříme si objekty

frog = Frog()
cars = []

for lane_number, lane_y in enumerate(LANES_Y):
    lane_speed = 100 * random()
    if lane_number % 2 == 1:
        # liché pruhy pojedou zprava doleva, tj. proti směru osy X,
        # takže prostě použijeme negativní rychlost :)
        lane_speed = - lane_speed

    # určili jsme si informace o jízdním pruhu (směr a rychlost), teď do něj
    # vložíme auta:

    car_count = randrange(3, 10)
    for car_number in range(car_count):
        # vytvoříme nové auto, umístí se na náhodnou pozici ve směru X
        new_car = Car(x=randrange(WINDOW_WIDTH), y=lane_y, speed=lane_speed)
        # auto ale použijeme (přidáme do seznamu aut), jen když se nepřekrývá s jiným autem
        new_car_ok = True
        for already_present_car in cars:
            if sprites_overlap(new_car.sprite, already_present_car.sprite, gap=MIN_GAP):
                new_car_ok = False
        if new_car_ok:
            cars.append(new_car)


window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)


def tik(time_since_last_call):
    for car in cars:
        car.tick(time_since_last_call)
    kill_frog = False
    for car in cars:
        if sprites_overlap(car.sprite, frog.sprite):
            kill_frog = True
    if kill_frog:
        frog.killed()


pyglet.clock.schedule_interval(tik, 1/50)


background_sprite = pyglet.sprite.Sprite(img_background)

game_won_text = pyglet.text.Label('YOU WON!',
                          font_name='Times New Roman',
                          font_size=50,
                          x=100, y=WINDOW_HEIGHT // 2)


game_over_text = pyglet.text.Label('GAME OVER',
                          font_name='Times New Roman',
                          font_size=50,
                          x=100, y=WINDOW_HEIGHT // 2)

remaining_lives_text = pyglet.text.Label('X',
                          font_name='Times New Roman',
                          font_size=21,
                          x=80, y=10)


def handle_draw():
    window.clear()
    background_sprite.draw()
    if frog.remaining_lives > 0:
        frog.draw()
        remaining_lives_text.text = str(frog.remaining_lives)
        remaining_lives_text.draw()
    for car in cars:
        car.draw()
    if frog.remaining_lives <= 0:
        game_over_text.draw()
    elif frog.finish_reached():
        game_won_text.draw()



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
