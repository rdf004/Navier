from random import randint
import random
from tqdm import tqdm
#Car Object Constructor
class Car(object):
    lane = 0
    distance = 0
    speed = 0

    def __init__(self, lane, distance, speed):
        self.lane = lane
        self.distance = distance
        self.speed = speed

def createCar(lane, distance, speed):
    car = Car(lane, distance, speed)
    return car


#Car Batch Creator
MILE = 5280
num_cars = 10000
carList = []
epochs = 10
lane1 = {'speed':random.uniform(8.1,12.1),'carCount':0}
lane2 = {'speed':random.uniform(8.1,12.1),'carCount':0}
lane3 = {'speed':random.uniform(8.1,12.1),'carCount':0}

laneChange = 0

lanes = [lane1,lane2,lane3]

segmentLength = 2*MILE

carLength = 15
#Our System
for i in range(0, num_cars):
    distance = randint(1,40)
    if distance > 5 and distance < 7:
        lane = 1
        speed = 45
        laneChange = laneChange + 1
    elif distance > 25 and distance < 27:
        lane = 2
        speed = 65
        laneChange = laneChange + 1
    else:
        lane = 3
        speed = 75
    car = Car(lane,distance,speed)
    carList.append(car)


print laneChange
print 'Lane 1: ' + str(lane1['carCount'])
print 'Lane 2: ' + str(lane2['carCount'])
print 'Lane 3: ' + str(lane3['carCount'])
