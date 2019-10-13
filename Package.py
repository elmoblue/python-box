from record import Record

class Package:

    def __init__(self):
        self.event_id = ''
        self.event_name = ''
        self.location = ''
        self.duration_hours = ''
        self.head_rate = ''
        self.inclusion = ''

    def __repr__(self):
        return "Package: {}".format(self.event_name)

    def setEventName(self, args):
        self.event_name = args

    def setLocation(self, args):
        self.location = args

    def setDuration(self, args):
        self.duration_hours = args

    def setRate(self, args):
        self.head_rate = args

    def addInclusion(self, args):
        self.inclusion = args

    def save(self):
        query = "insert into packages(location, duration, head_rate, inclusion, event_name)" \
                "VALUES('{0}','{1}','{2}','{3}','{4}');".format(self.location, self.duration_hours, self.head_rate, self.inclusion, self.event_name)
        Record.runQuery(query)

    @staticmethod
    def getbyID(packageID):
        query = "select * from packages where package_id = ('{}');".format(packageID)
        packageRecord = Record.fetchSingleRecord(query)
        package = Package()
        package.event_id = packageRecord[0]
        package.location = packageRecord[1]
        package.duration_hours = packageRecord[2]
        package.head_rate = packageRecord[3]
        package.inclusion = packageRecord[4]
        package.event_name = packageRecord[5]

        return package