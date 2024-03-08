'Game: guess number'
import numpy as np
number = np.random.randint(1, 101)

count = 0

while True:
    count+=1
    predict_number = int(input('Guess a number between 1 and 100: '))
    if predict_number == number:
        print(f'Correct guess! It was took a {count} tries!')
        break