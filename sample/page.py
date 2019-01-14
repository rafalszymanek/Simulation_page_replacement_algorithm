class Page:
    def __init__(self, id):
        self.id = id
        self.numberOfOld = 0
        self.numberOfAttempt = 0

    def checkId(self):
        return self.id

    def usePageLRU(self, attempt):
        self.numberOfOld = attempt

    def usePageLFU(self, attempt):
        self.numberOfOld = attempt
        self.numberOfAttempt += 1

    def checkNumberOfAtempt(self):
        return self.numberOfOld
