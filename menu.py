
class Menu:
    def __init__(self):
        self.fname = ''
        self.lname = ''
        self.fullname = ''
        self.fullname = ''

    def setFname(self, fname):
        self.fname = fname

    def setLname(self, lname):
        self.lname = lname

    def getFullname(self):
        self.fullname = self.fname + ' ' + self.lname