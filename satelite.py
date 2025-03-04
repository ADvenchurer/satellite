import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
lines = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

number_of_satellites = 8

def create_sattelites():
    global start_time
    for count in range(0,number_of_satellites):
        satellite = Actor("")
        satellite.pos = randint(40,WIDTH-40), rantint(40,HEIGHT-40)
        satellite,append(satellites)
    start_time = time()


def draw():
    global total_time
    screen.blit("background", (0,0))
    number = 1
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0], satellite.pos[1]+20))
        satellite.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_satellite < number_of_satellites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize = 30)

    