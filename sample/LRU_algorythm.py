from sample.page_LRU import PageLRU
from sample.frames import Frames


class LruAlgorythm:
    def __init__(self, number):
        self.ramka = Frames(number)
        self.queueOfPages = [1, 20, 1, 1, 11, 15]
        self.listOfPages = []

    def doAlgorythm(self):
        for i in range(20): # To easiest way index 0 will be never used
            self.listOfPages.append(PageLRU(i))

        for page in self.queueOfPages:
            if self.ramka.checkIsPagesIdInFrames(page):
                print(True)
            else:
                print("wkładam do ramki" + str(page))
                self.ramka.addPageIdToFrame(page)
                self.ramka.addPageFault()

        print(self.ramka.pageFault)
