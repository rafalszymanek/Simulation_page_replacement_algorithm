from sample.page_LRU import PageLRU
from sample.frames import Frames


def lruAlgorythm():
    ramka = Frames(3)
    queueOfPages = [1, 20, 4, 1, 11, 15]
    listOfPages = []

    for i in range(20):
        listOfPages.append(PageLRU(i))




    for page in queueOfPages:
        ramka.checkIsPagesIdInFrames(page)
