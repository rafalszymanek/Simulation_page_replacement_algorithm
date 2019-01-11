class PageLRU:
    def __init__(self, id):
        self.id = id
        self.numberOfOld = 0

    def checkId(self):
        return self.id

    def usePage(self, attempt):
        self.numberOfOld = attempt

    def checkNumberOfAtempt(self):
        return self.numberOfOld
