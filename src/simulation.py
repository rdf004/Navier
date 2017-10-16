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
'''Our System

for i in range(0, num_cars):
    distance = randint(1,1000)
    if distance < 5:
        lane = 1
        speed = 45
    elif distance < 25:
        lane = 2
        speed = 65
    else:
        lane = 3
        speed = 75

    car = Car(lane,distance,speed)

    carList.append(car)
'''

for i in tqdm(range(0, num_cars)):

    laneNum = randint(0,2)
    if laneNum == 0:
        lane1['carCount'] += 1
    elif laneNum == 1:
        lane2['carCount'] += 1 
    else:
        lane3['carCount'] += 1
    car = Car(laneNum + 1,230,lanes[laneNum]['speed'])

    carList.append(car)

''' Based off Speed
for i in range(0,len(carList)):

    if carList[i].lane == 3:
        
        if lane2['speed'] > lane3['speed'] and randint(0,1) == 1:
            laneChange+=1 
            lane3['speed'] += 0.5
            lane2['speed'] -= 0.5 
            lane3['carCount'] -= 1
            lane2['carCount'] += 1  

    elif carList[i].lane == 2:
        if lane3['speed'] > lane2['speed'] and randint(0,1) == 1:
            laneChange+=1
            lane3['speed'] -= 0.5
            lane2['speed'] += 0.5
            lane2['carCount'] -= 1
            lane3['carCount'] += 1  
        elif lane1['speed'] > lane2['speed'] and randint(0,1) == 1:
            laneChange+=1
            lane2['speed'] -= 0.5
            lane2['speed'] += 0.5
            lane2['carCount'] -= 1
            lane1['carCount'] += 1  
    else:
        if lane2['speed'] > lane1['speed'] and randint(0,1) == 1:
            laneChange+=1
            lane1['speed'] += 0.5
            lane2['speed'] -= 0.5
            lane1['carCount'] -= 1
            lane2['carCount'] += 1  
print laneChange
print 'Lane 1: ' + str(lane1['carCount'])
print 'Lane 2: ' + str(lane2['carCount'])
print 'Lane 3: ' + str(lane3['carCount'])

'''
for i in range(0,len(carList)):

    if carList[i].lane == 3:
        
        if lane2['carCount'] < lane3['carCount'] and randint(0,1) == 1:
            laneChange+=1 
            lane3['carCount'] -= 1
            lane2['carCount'] += 1  

    elif carList[i].lane == 2:
        if lane3['carCount'] < lane2['carCount'] and randint(0,1) == 1:
            laneChange+=1
            lane2['carCount'] -= 1
            lane3['carCount'] += 1  
        elif lane1['carCount'] < lane2['carCount'] and randint(0,1) == 1:
            laneChange+=1
            lane2['carCount'] -= 1
            lane1['carCount'] += 1  
    else:
        if lane2['carCount'] < lane1['carCount'] and randint(0,1) == 1:
            laneChange+=1
            lane1['carCount'] -= 1
            lane2['carCount'] += 1  
print laneChange
print 'Lane 1: ' + str(lane1['carCount'])
print 'Lane 2: ' + str(lane2['carCount'])
print 'Lane 3: ' + str(lane3['carCount'])