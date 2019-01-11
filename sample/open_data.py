

def openFileAndPutIntoMatrix(path):
    width, height = checkWidthAndHeightOfFile(path)
    matrix = [[0 for x in range(width)] for y in range(height)]
    fileWithData = open(path, "r")

    actualAttempt = 0
    for line in fileWithData:
        ourList = (list(map(int, line.split())))
        for j in range(0,width):
            matrix[actualAttempt][j] = ourList[j]
        actualAttempt+=1

    fileWithData.close()
    return matrix

def checkWidthAndHeightOfFile(path):
    fileWithData = open(path, "r")
    width = 0
    height = 0

    for line in fileWithData:
        ourList = (list(map(int, line.split())))
        height += 1
        width = len(ourList)

    fileWithData.close() # File automaticly close when we exit function
    return width, height
