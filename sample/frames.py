class Frames():
    def __init__(self, size):
        self.listOfFrames = [0] * size
        self.pageFault = 0

    def checkIsPagesIdInFrames(self,pageId):
        for frame in self.listOfFrames:
            if frame == pageId:
                return True

        return False

    def addPageIdToFrame(self, pageId):
        i = 0
        for frame in self.listOfFrames:
            if frame == 0:
                self.listOfFrames[i] = pageId
                break;
            i+=1

    def addPageFault(self):
        self.pageFault+=1
