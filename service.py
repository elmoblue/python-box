from record import Record


# noinspection SqlResolve
class Services:


    def __init__(self):
        self.servicesid = ''
        self.servicesname = ''
        self.servicesprice = ''
        self.miscellaneous = ''

    def __repr__(self):
            return "Package: {}".format(self.servicesname)

    def setServicesName(self, args):
            self.servicesname = args

    def setServicesPrice(self, args):
            self.servicesprice = args

    def setMiscellaneous(self, args):
            self.miscellaneous = args

    def save(self):
        query = "insert into services(servicename, serviceprice, miscellaneous)" \
                    "VALUES('{0}','{1}','{2}');".format(self.servicesname, self.servicesprice, self.miscellaneous)
        Record.runQuery(query)

    @staticmethod
    def getbyID(servicesID):
            query = "select * from services where serviceid = ('{}');".format(servicesID)
            servicesRecord = Record.fetchSingleRecord(query)
            services = Services()
            services.servicesid = servicesRecord[0]
            services.servicesname = servicesRecord[1]
            services.servicesprice = servicesRecord[2]
            services.miscellaneous = servicesRecord[3]

            return services

    @staticmethod
    def getRecords():
        query = "select * from services;"
        serivceRecords = Record.fetchAllRecord(query)

        return serivceRecords

    @staticmethod
    def printServices():
        Records = Services.getRecords()

        print("-----------------------------------------------------SERVICES------------------------------------------------------------")
        for row in Records:
            print('| ID: {} | Service Name: {} | Price: {} | Miscellaneous: {} | '.format(row[0], row[1], row[2], row[3]))
            print("-----------------------------------------------------------------------------------------------------------------------------")