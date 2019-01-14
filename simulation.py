from sample.LRU_algorythm import *
from sample.LFU_algorythm import *
from sample.open_data import *
from statistics import mean

path = "data/pages1.csv"
matrix = openFileAndPutIntoMatrix(path)

width, height = checkWidthAndHeightOfFile(path)


####################
# LFU
####################
print ("------------\nLRU\n------------\n")

lruResult3 = []
algorytm = LruAlgorythm(3)
for row in range(height):
    lruResult3.append(algorytm.doAlgorythm(matrix[row]))
print ("Srednia dla tablicy 3 elementowej: "+str(mean(lruResult3)))


lruResult5 = []
algorytm = LruAlgorythm(5)
for row in range(height):
    lruResult5.append(algorytm.doAlgorythm(matrix[row]))
print ("Srednia dla tablicy 5 elementowej: "+str(mean(lruResult5)))


lruResult7 = []
algorytm = LruAlgorythm(7)
for row in range(height):
    lruResult7.append(algorytm.doAlgorythm(matrix[row]))
print ("Srednia dla tablicy 7 elementowej: "+str(mean(lruResult7)))


####################
# LFU
####################
print ("------------\nLFU\n------------\n")

lfuResult3 = []
algorytm = LfuAlgorythm(3)
for row in range(height):
    lfuResult3.append(algorytm.doAlgorythm(matrix[row]))
print ("Srednia dla tablicy 3 elementowej: "+str(mean(lfuResult3)))


lfuResult5 = []
algorytm = LfuAlgorythm(5)
for row in range(height):
    lfuResult5.append(algorytm.doAlgorythm(matrix[row]))
print ("Srednia dla tablicy 5 elementowej: "+str(mean(lfuResult5)))


lfuResult7 = []
algorytm = LfuAlgorythm(7)
for row in range(height):
    lfuResult7.append(algorytm.doAlgorythm(matrix[row]))
print ("Srednia dla tablicy 7 elementowej: "+str(mean(lfuResult7)))
