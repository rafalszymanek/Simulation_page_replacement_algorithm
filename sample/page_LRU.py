class PageLRU:
    def __init__(self, id):
        self.id = id
        self.pageOld = 0

    def checkId(self):
        return self.id

    def usePage(self):
        self.pageOld = 0

    def incresePageOld(self):
        self.pageOld+=1

    def checkPageOld(self):
        return self.pageOld
