class Frames():
    def __init__(self, size):
        self.listOfFrames = [0] * size   # List Of All frames not a class, it's a int
        self.pageFault = 0

    def checkIsPagesIdInFrames(self, pageId):
        for frame in self.listOfFrames:
            if frame == pageId:
                return True
        return False

    def addPageIdToFrame(self, pageId, indexPageToChange):
        self.listOfFrames[indexPageToChange] = pageId

    def addPageFault(self):
        self.pageFault+=1
