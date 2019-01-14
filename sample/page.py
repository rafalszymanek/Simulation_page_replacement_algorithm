class Page:
    """
    Class taht simulate page in operation system.
    Only for mathematical simulation.
    """
    def __init__(self, id):
        """
        int id - is current id of page
        int numberOfOld - how long this page is in frame
        int numberOfAttempt - how many times this page was in frame
        """
        self.id = id
        self.numberOfOld = 0
        self.numberOfAttempt = 0

    def checkId(self):
        """
        Returns id of page
        """
        return self.id

    def usePageLRU(self, attempt):
        """
        Use page as LRU algorythm
        set numberOfOld to current attempt of simulation
        """
        self.numberOfOld = attempt

    def usePageLFU(self, attempt):
        """
        Use page as LRU algorythm
        set numberOfOld to current attempt of simulation
        set self.numberOfAttempt increment by one
        """
        self.numberOfOld = attempt
        self.numberOfAttempt += 1

    def checkNumberOfAtempt(self):
        """
        Returns numberOfOld
        """
        return self.numberOfOld
