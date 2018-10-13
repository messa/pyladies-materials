import pyglet
from random import choice, random, randrange
from math import sin


WIDTH, HEIGHT = 640, 480
FROG_WIDTH, FROG_HEIGHT = 32, 32
CAR_WIDTH, CAR_HEIGHT = 32, 32
FROG_STEP = 32
START_LINE_Y = 40
FINISH_LINE_Y = 424
LANES_Y = [72, 104, 136, 200, 232, 264, 328, 360, 392]
LTR = 1
RTL = -1
LANES_DIRECTION = [LTR if n % 2 == 0 else RTL for n in range(len(LANES_Y))]
LANES_SPEED = [2 + 3 * random() for _ in LANES_Y]
CAR_COUNT_START = 20
CAR_COUNT_MAX = 40


img_background = pyglet.image.load('images/pozadi.bmp')
#img_frog_left = pyglet.image.load('images/frog1.bmp')
#img_frog_right = pyglet.image.load('images/frog2.bmp')
img_frog_up = pyglet.image.load('images/frog3.bmp')
#img_frog_down = pyglet.image.load('images/frog4.bmp')

img_cars = [pyglet.image.load(f'images/{i}.bmp') for i in range(1, 13)]

background_sprite = pyglet.sprite.Sprite(img_background)


def within_bounds(value, lower_bound, upper_bound):
    value = max(value, lower_bound)
    value = min(value, upper_bound)
    return value


class Frog:

    def __init__(self):
        frog_img = img_frog_up.get_region(0, 0, FROG_WIDTH, FROG_HEIGHT)
        self.sprite = pyglet.sprite.Sprite(frog_img)
        self.sprite.x = WIDTH // 2
        self.sprite.y = START_LINE_Y

    def draw(self):
        self.sprite.draw()

    def go_left(self):
        self._go(-FROG_STEP, 0)

    def go_right(self):
        self._go(FROG_STEP, 0)

    def go_up(self):
        # souradnice Y=0 je spodni hrana, takze UP je pricitani Y
        self._go(0, FROG_STEP)

    def go_down(self):
        # souradnice Y=0 je spodni hrana, takze DOWN je odcitani Y
        self._go(0, -FROG_STEP)

    def _go(self, dx, dy):
        self.sprite.x = within_bounds(self.sprite.x + dx, 0, WIDTH)
        self.sprite.y = within_bounds(self.sprite.y + dy, START_LINE_Y, FINISH_LINE_Y)
        print('New frog position:', self.sprite.x, self.sprite.y)
        if self.sprite.y >= FINISH_LINE_Y:
            print('Finish!')

    def get_collision_box(self):
        return (
            self.sprite.x,
            self.sprite.x + CAR_WIDTH,
            self.sprite.y,
            self.sprite.y + CAR_HEIGHT,
        )


class Car:

    def __init__(self, initial=False):
        lane_number = randrange(len(LANES_Y))
        self.direction = LANES_DIRECTION[lane_number]
        self.speed = LANES_SPEED[lane_number]
        self.sprite = pyglet.sprite.Sprite(choice(img_cars))
        if initial:
            self.sprite.x = randrange(WIDTH)
        elif self.direction == LTR:
            self.sprite.x = - CAR_WIDTH
        elif self.direction == RTL:
            self.sprite.x = WIDTH
        self.sprite.y = LANES_Y[lane_number]

    def get_collision_box(self):
        return (
            self.sprite.x,
            self.sprite.x + CAR_WIDTH,
            self.sprite.y,
            self.sprite.y + CAR_HEIGHT,
        )

    def draw(self):
        self.sprite.draw()

    def tick(self, time_since_last_call):
        self.sprite.x += self.speed * self.direction

    def off_grid(self):
        return self.sprite.x + CAR_WIDTH < 0 or self.sprite.x > WIDTH


def objects_overlap(a, b, x_gap=0):
    a_x_min, a_x_max, a_y_min, a_y_max = a.get_collision_box()
    b_x_min, b_x_max, b_y_min, b_y_max = b.get_collision_box()
    assert a_x_min < a_x_max and a_y_min < a_y_max
    assert b_x_min < b_x_max and b_y_min < b_y_max
    if a_x_max + x_gap <= b_x_min or b_x_max + x_gap <= a_x_min:
        # objekty jsou mimo horizontalne
        return False
    if a_y_max <= b_y_min or b_y_max <= a_y_min:
        # objekty jsou mimo vertikalne
        return False
    # objekty se prekryvaji
    return True


frog = Frog()

cars = []


def try_add_new_car(initial):
    new_car = Car(initial=initial)
    if all(not objects_overlap(new_car, car, x_gap=10) for car in cars):
        cars.append(new_car)


# vyplnime nejaka auta
while len(cars) < CAR_COUNT_START:
    try_add_new_car(initial=True)



window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


def tik(time_since_last_call):
    global cars
    for car in cars:
        car.tick(time_since_last_call)
    cars = [car for car in cars if not car.off_grid()]
    if any(objects_overlap(frog, car) for car in cars):
        print('Zaba byla zajeta!')
        pyglet.app.exit()
    if len(cars) < CAR_COUNT_MAX and random() * time_since_last_call < 3:
        try_add_new_car(initial=False)


pyglet.clock.schedule_interval(tik, 1/30)


def handle_draw():
    window.clear()
    background_sprite.draw()
    frog.draw()
    for car in cars:
        car.draw()


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
