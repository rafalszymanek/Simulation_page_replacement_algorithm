class Frames():
    """
    Class that simulate (only for mathematical purpose) Frames.
    It's scalable list that conteins only ID numbers of pages that is actualy in frame.
    """
    def __init__(self, size):
        """
        List Int listOfFrames - Contains all ID numbers of pages that is actualy in frame.
        Int pageFault - Contain how many page fault was in current attempt
        """
        self.listOfFrames = [0] * size   # List Of All frames not a class, it's a int
        self.pageFault = 0

    def checkIsPagesIdInFrames(self, pageId):
        """
        That function check there is this page contain id of searching pageID.
        Returns True or False
        """
        for frame in self.listOfFrames:
            if frame == pageId:
                return True
        return False

    def addPageIdToFrame(self, pageId, indexPageToChange):
        """
        Add or Replace ID number of page to our frame.
        It replace by id of witch index is need to change.
        """
        self.listOfFrames[indexPageToChange] = pageId

    def addPageFault(self):
        """
        increment by one pageFault
        """
        self.pageFault+=1
