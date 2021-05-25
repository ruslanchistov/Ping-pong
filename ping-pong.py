""" Игра пин понг """

from turtle import *


border_up = 290
border_down = -280
border_left = -390
border_right = 380
length_racket = 50
max_y_move = 240
move = 20
play = True


def create_racket(racket, color_, x):
    racket.shape("square")                            # задаём форму ракетки - прямоугольник.
    racket.speed(0)                                   # задаём скорость ракетки.
    racket.color(color_)                              # задаём цвет ракетки.
    racket.shapesize(stretch_len=0.5, stretch_wid=5)  # задаём размеры ракетки (толщина,длина).
    racket.penup()                                    # чтобы ракетка не оставляла след при движении.
    racket.goto(x, 0)                                 # задаём начальное положение ракетки.


""" Функции движения """


def racket_a_up():              # движение левой ракетки вверх.
    y = racket_a.ycor()         # определяем положение ракетки по y.
    if y < max_y_move:          # ограничиваем движение ракетки вверх.
        y += move               # изменяем значение y.
        racket_a.sety(y)        # задаём новое значение y.


def racket_a_down():            # движение левой ракетки вниз.
    y = racket_a.ycor()         # определяем положение ракетки по y.
    if y > -max_y_move:         # ограничиваем движение ракетки вниз.
        y -= move               # изменяем значение y.
        racket_a.sety(y)        # задаём новое значение y.


def racket_b_up():              # движение правой ракетки вверх.
    y = racket_b.ycor()         # определяем положение ракетки по y.
    if y < max_y_move:          # ограничиваем движение ракетки вверх.
        y += move               # изменяем значение y.
        racket_b.sety(y)        # задаём новое значение y.


def racket_b_down():            # движение правой ракетки вниз.
    y = racket_b.ycor()         # определяем положение ракетки по y.
    if y > -max_y_move:         # ограничиваем движение ракетки вниз.
        y -= move               # изменяем значение y.
        racket_b.sety(y)        # задаём новое значение y.


""" Создаём окно """
win = Screen()                    # создали экземпляр класса Screen.
win.title("My ping pong")         # выводим заголовок окна.
win.bgcolor("black")              # задаём цвет фона окна.
win.setup(width=800, height=600)  # задаём размеры окна (ширина,высота).
win.tracer(0)

""" Создаём левую ракетку """
racket_a = Turtle()                                 # создаём экземпляр класса Turtle.
create_racket(racket_a, 'blue', -385)

""" Создаём правую ракетку """
racket_b = Turtle()                                 # создаём экземпляр класса Turtle.
create_racket(racket_b, "yellow", 380)


""" Создаём шарик """
ball = Turtle()                                     # создаём экземпляр класса Turtle.
ball.shape("circle")                                # задаём форму шарика - прямоугольник.
ball.speed(0)                                       # задаём начальную скорость шарика.
ball.color("white")                                 # задаём цвет шарика.
ball.penup()                                        # чтобы шарик не оставлял след при движении.
ball.goto(0, 0)                                     # задаём начальное положение шарика.
ball.dx = 1.0                                       # задаём скорость шарика по х.
ball.dy = 1.0                                       # задаём скорость шарика по у.


""" Счётчик очков """
count = Turtle()                                    # создаём экземпляр класса Turtle.
count.color("white")                                # задаём цвет табло.
count.penup()                                       # чтобы не было следов прорисовки табло.
count.shape("square")                               # задаём форму табло - прямоугольник.
count.speed(0)                                      # задаём скорость табло (неподвижное).
count.goto(0, 260)                                  # задаём место расположения табло.
count.write("Player A: 0  Player B: 0", align="center", font=("Verdana", 22, "normal"))  # выводим текст табло.
count.hideturtle()                                  # скрываем маркер прорисовки табло.
goal_A = 0                                          # объявляем счётчик голов в пользу левой ракетки.
goal_B = 0                                          # объявляем счётчик голов в пользу правой ракетки.


""" Определяем работу клавиатуры """


win.listen()
win.onkeypress(racket_a_up, 'w')
win.onkeypress(racket_a_down, 's')
win.onkeypress(racket_b_up, 'p')
win.onkeypress(racket_b_down, 'l')

""" Цикл для того, чтобы окно не закрывалось """
while play:
    try:
        win.update()

        """ Движение шарика """
        ball.setx(ball.xcor() + ball.dx)  # установить значение х (запросить настоящее значение х и изменить его на dx).
        ball.sety(ball.ycor() + ball.dy)  # установить значение y (запросить настоящее значение y и изменить его на dy).

        """ Отскакивание шарика от стенок """
        if ball.ycor() > border_up:         # проверяем каснулся ли шарик верхней границы поля.
            ball.sety(border_up)
            ball.dy *= -1                   # если каснулся, то отскакивает.

        if ball.ycor() < border_down:       # проверяем каснулся ли шарик нижней границы поля.
            ball.sety(border_down)
            ball.dy *= -1                   # если каснулся, то отскакивает.

        if ball.xcor() > border_right:      # проверяем каснулся ли шарик правой границы поля.
            ball.setx(border_right)
            ball.dx *= -1                   # если каснулся, то отскакивает.
            goal_A += 1                     # увеличиваем счётчик голов в пользу левой ракетки.
            count.clear()                   # очищаем табло.

            # выводим новое значение счёта.
            count.write("Player A: {}  Player B: {}".format(goal_A, goal_B), align="center",
                        font=("Verdana", 22, "normal"))

        if ball.xcor() < border_left:       # проверяем каснулся ли шарик левой границы поля.
            ball.setx(border_left)
            ball.dx *= -1                   # если каснулся, то отскакивает.
            goal_B += 1                     # увеличиваем счётчик голов в пользу правой ракетки.
            count.clear()                   # очищаем табло.

            # выводим новое значение счёта.
            count.write("Player A: {}  Player B: {}".format(goal_A, goal_B), align="center",
                        font=("Verdana", 22, "normal"))

        """ Отскакивание шарика от ракеток """

        if ball.xcor() > 365 and (ball.ycor() > racket_b.ycor() - length_racket) and \
                (ball.ycor() < racket_b.ycor() + length_racket):
            ball.dx *= -1
        if ball.xcor() < -365 and (ball.ycor() > racket_a.ycor() - length_racket) and \
                (ball.ycor() < racket_a.ycor() + length_racket):
            ball.dx *= -1
    except Exception:
        play = False
