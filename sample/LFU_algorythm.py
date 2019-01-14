from sample.page import Page
from sample.frames import Frames


class LfuAlgorythm:
    """
    This is a class of LFU page preplacement of modern operating systems.
    This only simulate how many page fault is in our attempt.
    """
    def __init__(self, number):
        """
        int number
        Frames frame - our object of all frames in memory
        list listOfPages - list of classes "Page", it contain all pages in operating system.
        int attempt - number of actual attempt (row of matrix)
        """
        self.number = number
        self.frame = Frames(number)
        self.listOfPages = []
        self.attempt = 1


    def doAlgorythm(self, queueOfPages):
        """
        It control of all exec of algorythm
        - Create list of Pages contain classes "Page"
        - Do algorythm for each page in queueOfPages
        - Replace pages in frames

        Return number of page fault of attempt
        """
        self.frame = Frames(self.number)
        self.listOfPages = []
        self.attempt = 1

        for i in range(21): # To easiest way index 0 will be never used. !20! is max value
            self.listOfPages.append(Page(i))

        for page in queueOfPages:
            # print ("Ramki: " + str(self.frame.listOfFrames))
            # print ("Chce wejsc: " + str(page))

            self.usePage(page)
            if not(self.frame.checkIsPagesIdInFrames(page)):
                indexPageToChange = self.findLeastFrequently()
                # print("Ineks do zastapienia: " + str(indexPageToChange))
                self.frame.addPageIdToFrame(page, indexPageToChange)
                self.frame.addPageFault()

        return self.frame.pageFault


    def usePage(self, pageId):
        """
        Simulate use of page
        Add attempt to page of current ID
        Add number of old current page ID in frame
        """
        self.listOfPages[pageId].usePageLFU(self.attempt)
        self.attempt += 1


    def findLeastFrequently(self):
        """
        All main implementation of algorythm LFU
        Serach Least Frequently page in listOfFrames
        If is equal search choose to change that one with is longer in frame.

        Returns what idex is to change
        """
        minOldNumber = self.listOfPages[int(self.frame.listOfFrames[0])].numberOfOld    # First element of Frames
        minNumberOfAttempt = self.listOfPages[int(self.frame.listOfFrames[0])].numberOfAttempt
        indexPageToChange = 0

        i = 0
        for frame in self.frame.listOfFrames:
            if frame == 0:
                indexPageToChange = i
                break
            elif self.listOfPages[frame].numberOfAttempt < minNumberOfAttempt:
                minNumberOfAttempt = self.listOfPages[frame].numberOfAttempt
                minOldNumber = self.listOfPages[frame].numberOfOld
                indexPageToChange = i
            elif self.listOfPages[frame].numberOfAttempt == minNumberOfAttempt:
                if self.listOfPages[frame].numberOfOld < minOldNumber:
                    minOldNumber = self.listOfPages[frame].numberOfOld
                    indexPageToChange = i
            i+=1
        return indexPageToChange
