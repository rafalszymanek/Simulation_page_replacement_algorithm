from sample.page_LRU import PageLRU
from sample.frames import Frames


class LruAlgorythm:
    def __init__(self, number):
        self.number = number
        self.ramka = Frames(number)
        self.listOfPages = []
        self.attempt = 1

    def doAlgorythm(self, queueOfPages):
        self.ramka = Frames(self.number)
        self.listOfPages = []
        self.attempt = 1

        for i in range(21): # To easiest way index 0 will be never used. !20! is max value
            self.listOfPages.append(PageLRU(i))


        for page in queueOfPages:
            # print ("Ramki: " + str(self.ramka.listOfFrames))
            # print ("Chce wejść: " + str(page))

            self.usePage(page)
            if self.ramka.checkIsPagesIdInFrames(page):
                # print("Strona znajduje się w ramce!")
                pass
            else:
                indexPageToChange = self.findLeastFrequently()
                # print("Ineks do zastąpienia: " + str(indexPageToChange))
                self.ramka.addPageIdToFrame(page, indexPageToChange)
                self.ramka.addPageFault()
            # print ("Ramki po zmianie: " + str(self.ramka.listOfFrames) + "\n\n")

        # print(self.ramka.pageFault)
        return self.ramka.pageFault




    def usePage(self, pageId):
        self.listOfPages[pageId].usePage(self.attempt)
        self.attempt += 1

    def findLeastFrequently(self):
        minOldNumber = 99999999
        indexPageToChange = 0

        i = 0
        for frame in self.ramka.listOfFrames:
            if frame == None:
                indexPageToChange = i
                break
            elif self.listOfPages[frame].numberOfOld < minOldNumber:
                minOldNumber = self.listOfPages[frame].numberOfOld
                indexPageToChange = i
            i+=1

        return indexPageToChange
