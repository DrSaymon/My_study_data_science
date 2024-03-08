'Game: guess number'
import numpy as np
number = np.random.randit(1, 101)

count = 0

while True:
    count+=1
    predict_number = int(input('Guess a number between 1 and 100'))