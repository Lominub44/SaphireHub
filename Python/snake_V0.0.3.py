import turtle
import time
import random

delay = 0.1
score = 0

# Fenster einrichten
wn = turtle.Screen()
wn.title("Snake Spiel")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Deaktiviere die automatische Aktualisierung des Bildschirms

# Schlangenkopf
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Essen erzeugen
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Schlangenkörper-Segmente
segments = []

# Score Label
score_label = turtle.Turtle()
score_label.speed(0)
score_label.color("white")
score_label.penup()
score_label.hideturtle()
score_label.goto(0, 260)
score_label.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Funktionen
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Tastaturbindungen
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Pfeiltasten zum Steuern der Schlange hinzufügen
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Hauptspiel-Schleife
while True:
    wn.update()

    # Kollision mit dem Rand
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"

        # Verstecke die Körperteile
        for segment in segments:
            segment.goto(1000, 1000)

        # Lösche die Körperteile-Liste
        segments.clear()

        # Reset Score
        score = 0
        score_label.clear()
        score_label.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Kollision mit dem Essen
    if head.distance(food) < 20:
        # Bewege das Essen an eine zufällige Position
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Füge ein Körperteil hinzu
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Erhöhe den Score
        score += 1
        score_label.clear()
        score_label.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Bewege die Körperteile in umgekehrter Reihenfolge
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Bewege das erste Körperteil zum Kopf
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Kollision mit dem eigenen Körper
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"

            # Verstecke die Körperteile
            for segment in segments:
                segment.goto(1000, 1000)

            # Lösche die Körperteile-Liste
            segments.clear()

            # Reset Score
            score = 0
            score_label.clear()
            score_label.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
