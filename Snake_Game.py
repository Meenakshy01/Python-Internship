import turtle
import random
import time

# Set up the screen
win = turtle.Screen()
win.title("Snake Game")
win.bgcolor("yellow")
win.setup(width=600, height=600)
win.tracer(0)  # Turns off screen updates

# Register the snake shape
win.register_shape("snake", ((0,0), (10,10), (10,0)))  # Example custom shape, adjust as needed

# Snake class
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((0 - i * 20, 0))

    def add_segment(self, pos):
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("snake")  # Use the custom shape
        segment.color("blue")
        segment.penup()
        segment.goto(pos)
        self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        # Clear existing segments
        for segment in self.segments:
            segment.goto(1000, 1000)  # Move segments out of the screen
            segment.clear()
        self.segments.clear()
        # Create new snake
        self.create_snake()

# Food class
class Food:
    def __init__(self):
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)

    def move_food(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.food.goto(x, y)

# Score class
class Score:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("black")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_scoreboard()

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Courier", 24, "normal"))

# Boundary checking
def check_boundary():
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        return True
    return False

# Self collision
def check_collision():
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 20:
            return True
    return False

# Main game
snake = Snake()
food = Food()
score = Score()

# Functions for key bindings
def go_up():
    snake.move_up()

def go_down():
    snake.move_down()

def go_left():
    snake.move_left()

def go_right():
    snake.move_right()

# Keyboard bindings for arrow keys
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

# Main game loop
while True:
    win.update()
    snake.move()
    time.sleep(0.1)

    # Check for collision with food
    if snake.head.distance(food.food) < 20:
        food.move_food()
        # Add new segment to snake
        snake.add_segment((0, 0))
        score.increase_score()

    # Check for collision with wall
    if check_boundary():
        score.reset()
        snake.reset()

    # Check for collision with self
    if check_collision():
        score.reset()
        snake.reset()
