from sample.LRU_algorythm import *
from sample.open_data import *
from statistics import mean

path = "data/test_values.txt"
matrix = openFileAndPutIntoMatrix(path)

width, height = checkWidthAndHeightOfFile(path)
lruResult3 = []

algorytm = LruAlgorythm(3)
for row in range(height):
    lruResult3.append(algorytm.doAlgorythm(matrix[row]))


print ("------------\nLRU\n------------\n")
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
