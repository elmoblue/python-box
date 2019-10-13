from record import Record


# noinspection SqlResolve
class User:
    def __init__(self):
        self.userid = ''
        self.fname = ''
        self.lname = ''
        self.fullname = ''

    def setFname(self, fname):
        self.fname = fname

    def setLname(self, lname):
        self.lname = lname

    def setFullname(self):
        self.fullname = self.fname + ' ' + self.lname

    def getFullname(self):
        return self.fullname

    def save(self):
        query = "insert into users(fname, lname)" \
                "VALUES('{0}','{1}');".format(self.fname, self.lname)
        Record.runQuery(query)

    @staticmethod
    def getbyID(userid):
        query = "select * from users where userid = ('{}');".format(userid)
        userRecord = Record.fetchSingleRecord(query)
        userModel = User()
        userModel.userid = userRecord[0]
        userModel.fname = userRecord[1]
        userModel.lname = userRecord[2]

        return userModel

    @staticmethod
    def getRecords():
        query = "select * from users;"
        userRecords = Record.fetchAllRecord(query)

        return userRecords

    @staticmethod
    def printUserRecords():
        Records = User.getRecords()

        print("-----------------------------------------------------USER RECORDS------------------------------------------------------------")
        for row in Records:
            print('| ID: {} | First Name: {} | Last Name: {} '.format(row[0], row[1], row[2]))
            print("-----------------------------------------------------------------------------------------------------------------------------")