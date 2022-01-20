import random
import csv
import math
import time
import uuid;

f = open('index.csv', 'w', newline='')

wr = csv.writer(f)
for i in range(20000000):
    tmp = [i+1 ,i+1, math.floor(random.random()*10000000), math.floor(time.time()), math.floor(time.time()), math.floor(random.random()*10)%2, str(uuid.uuid4())[:8]]
    wr.writerow(tmp)

