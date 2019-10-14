from user import User
from service import Services
from record import Record
import random


# noinspection SqlResolve
class Booking:
    def __init__(self):
        self.bookingID = ''
        self.serviceID = ''
        self.customerID = ''
        self.voucher_id = ''

    def save(self):
        query = "insert into bookings(serviceid, customerid, voucher_id)" \
                "VALUES('{0}','{1}','{2}');".format(self.serviceID, self.customerID, self.voucher_id)
        Record.runQuery(query)

    @staticmethod
    def generateVoucher():
        voucher_id = random.randint(1, 9999)

        return voucher_id

    @staticmethod
    def getbyVoucher(voucher_id):
        query = "select * from bookings where voucher_id = ('{}');".format(voucher_id)
        BookingRecord = Record.fetchSingleRecord(query)

        return BookingRecord

    @staticmethod
    def getRecords():
            query = "select * from bookings;"
            bookingsRecords = Record.fetchAllRecord(query)

            return bookingsRecords

    @staticmethod
    def printBookingRecords():
            bookingRecords = Booking.getRecords()
            print("-------------------------------------------------------------------------BOOKING RECORDS----------------------------------------------------------------------------------")
            for row in bookingRecords:
                userModel = User.getbyID(row[2])
                eventModel = Services.getbyID(row[1])
                fname = userModel.fname
                servicesname = eventModel.servicesname

                print('| Booking ID: {} | Service Name: {} |  First Name: {} | Miscellaneous: {} | Price: {} | Voucher ID: {} |'.format(row[0], servicesname, fname, eventModel.miscellaneous, eventModel.servicesprice, row[3]))
                print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

    @staticmethod
    def printSingleRecord(voucher_id):
        bookingRecords = Booking.getbyVoucher(voucher_id)
        print(
            "-------------------------------------------------------------------------BOOKING RECORDS----------------------------------------------------------------------------------")
        userModel = User.getbyID(bookingRecords[2])
        eventModel = Services.getbyID(bookingRecords[1])

        print(
                '| Booking ID: {} | Service Name: {} |  First Name: {} | Miscellaneous: {} | Price: {} | Voucher ID: {} |'.format(
                    bookingRecords[0], eventModel.servicesname, userModel.fname, eventModel.miscellaneous, eventModel.servicesprice, bookingRecords[3]))
        print(
                "--------------------------------------------------------------------------------------------------------------------------------------------------------------------------")


