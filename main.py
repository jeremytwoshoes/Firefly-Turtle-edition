import turtle
import random
import time

class firefly:
    MAXIMUM_GLOW = 1
    MINIMUM_GLOW = 0.01
    def __init__(self):
        self.neighbours = []
        self.position = (random.randint(0, 1920), random.randint(0, 1080))
        self.period = random.uniform(0, 5)
        self.clock = 0

    def glow(self):
        pass

def help(self):
    while True:
        turtle.dot(10, "purple")
        time.sleep(1)
        turtle.dot(20, "Purple")




turtle.hideturtle()
sc = turtle.Screen()
sc.setup(1920, 1080)
sc.bgcolor('white')

turtle.mainloop()
# turtle.done()
