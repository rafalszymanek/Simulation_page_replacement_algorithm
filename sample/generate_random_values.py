#Generate random values to list and put it to file

import random
import sys

processesInAttempt = int(input('How many processes in attempt[rows]?: '))
manyOfAttempt = int(input('How many attemts[columns]?: '))
toNumber = int(input('Random numbers from 1 to ?: '))
fromNumber = 1

with open("../data/random_values.txt", "w") as myfile:
    #range of random


    for i in range(manyOfAttempt):
        for j in range(processesInAttempt):
            randomNumber = random.randint(fromNumber,toNumber)
            myfile.write(str(randomNumber) + ' ')
        myfile.write('\n')

    myfile.close()
