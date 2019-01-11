class PageLRU:
    def __init__(self, id):
        self.id = id
        self.numberOfAtempt = 0

    def checkId(self):
        return self.id

    def usePage(self, attempt):
        self.numberOfAtempt = attempt

    def checkNumberOfAtempt(self):
        return self.numberOfAtempt
