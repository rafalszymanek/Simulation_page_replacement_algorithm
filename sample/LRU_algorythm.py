from sample.page import Page
from sample.frames import Frames


class LruAlgorythm:
    def __init__(self, number):
        self.number = number
        self.frame = Frames(number)
        self.listOfPages = []
        self.attempt = 1


    def doAlgorythm(self, queueOfPages):
        self.frame = Frames(self.number)
        self.listOfPages = []
        self.attempt = 1

        for i in range(21):     # To easiest way! index 0 will be never used. !20! is max value
            self.listOfPages.append(Page(i))

        for page in queueOfPages:
            # print ("Ramki: " + str(self.frame.listOfFrames))
            # print ("Chce wejść: " + str(page))

            self.usePage(page)
            if not(self.frame.checkIsPagesIdInFrames(page)):
                indexPageToChange = self.findLeastRecently()
                # print("Ineks do zastąpienia: " + str(indexPageToChange))
                self.frame.addPageIdToFrame(page, indexPageToChange)
                self.frame.addPageFault()
            # else:
                # print("Strona znajduje się w ramce!")
            # print ("Ramki po zmianie: " + str(self.frame.listOfFrames) + "\n\n")
            # print("Liczba błędów: " + str(self.frame.pageFault))
        # print(self.frame.pageFault)

        return self.frame.pageFault


    def usePage(self, pageId):
        self.listOfPages[pageId].usePageLRU(self.attempt)
        self.attempt += 1

    def findLeastRecently(self):
        minOldNumber = self.listOfPages[int(self.frame.listOfFrames[0])].numberOfOld    # First element of Frames
        indexPageToChange = 0

        i = 0
        for frame in self.frame.listOfFrames:
            if frame == 0:
                indexPageToChange = i
                break
            elif self.listOfPages[frame].numberOfOld < minOldNumber:
                minOldNumber = self.listOfPages[frame].numberOfOld
                indexPageToChange = i
            i+=1

        return indexPageToChange
