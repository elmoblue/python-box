from user import User
from record import Record
from service import Services
from booking import Booking

def option(message):
    key = raw_input("{}? [Y]es/[N]o: " . format(message))
    return key

def selection(args):
    if args == 1:
       login()
    elif args == 2:
        # register()
        menuselect()
    elif args == 3:
        exit()



def checkDB():
    Record.checkConnection()

def choose():
    print("WELCOME TO BDOT STUDIO")
    print("1. Admin")
    print("2. Customer")

# LoGin for admin user
def login():
    while True:
        userName = raw_input("Username: ")
        password = raw_input("Password: ")
        if userName == 'admin' and password == 'minda':
            adminMenuArgs()
        else:
            print("username or password inavlid!")
            print("Do you want to try again?")
            choice = raw_input("(Y)es or (N)o")
            if (choice == "y") or (choice == "Y"):
                continue
            else:
                start()

def adminMenu():
    print("----------------------")
    print("SELECT YOUR MENU:")
    print("1. ADD USER")
    print("2. ADD SERVICES")
    print("3. ADD BOOKING")
    print("4. EXIT")
    print("----------------------")

def adminMenuArgs():
    adminMenu()
    try:
        args = int(raw_input("PLEASE SELECT YOUR OPTION: "))
        adminMenuSelection(args)
    except ValueError:
        print("\n")
        print("ERROR! PLEASE CHOOSE THE CORRECT OPTION FROM THE MENU!")
        adminMenu()

# args for adminMenu
def  adminMenuSelection(args):
    if args == 1:
        register()
    elif args == 2:
        services()
    elif args == 3:
        booking()
    elif args == 4:
        start()

def admin():
    print("Bookings")
    print("----------------------")
    booking()
    print("----------------------")
    print("Do you want to exit?")
    choice = raw_input("(Y)es or (N)o")
    print()
    if (choice == "y") or (choice == "Y"):
        start()
    else:
        admin()

# adminMenu register
def register():
    model = User()
    model.setFname(raw_input("First Name: "))
    model.setLname(raw_input("Last Name: "))
    choice = option("Would you like to save changes")
    if choice == "Y":
        model.save()
        print("User successfully saved!")
    else:
        start()
    choice = option("Would you like to register more user")
    if choice == "Y":
        register()
    else:
        adminMenuArgs()

# adminMenu booking
def booking():
    User.printUserRecords()
    userID = int(raw_input("Please enter the id of the user to book: "))
    Services.printServices()
    servicesID = int(raw_input("Please enter the id of the service chosen by the customer: "))

    userObject = User.getbyID(userID)
    serviceObject = Services.getbyID(servicesID)
    bookingObject = Booking()
    bookingObject.customerID = userObject.userid
    bookingObject.serviceID = serviceObject.servicesid
    bookingObject.voucher_id = Booking.generateVoucher()

    choice = option("Would you like to save changes")
    if choice == "Y":
        bookingObject.save()
        print("Event records successfully saved!")
        print("Voucher ID: {}" .format(bookingObject.voucher_id))
        print("Please keep the voucher number for booking reference! ")
    else:
        start()
    choice = option("Would you like to add more booking")
    if choice == "Y":
        booking()
    else:
        adminMenuArgs()

def echobooking():
    Booking.printBookingRecords()

def menu():
    print("----------------------")
    print("PLEASE SELECT OPTION")
    print("1. REGISTER")
    print("2. VIEW BOOKINGS")
    print("3. EXIT")
    print("----------------------")

# userMenuSelection
def check(args):
    if args == 1:
        register()
    elif args == 2:
        # echobooking()
        userViewBooking()
    elif args == 3:
        exit()

# adminMenu services
def services():
    service = Services()
    service.setServicesName(raw_input("Service Name: "))
    service.setServicesPrice(raw_input("Price: "))
    service.setMiscellaneous(raw_input("Miscellaneous: "))

    choice = option("Would you like to save changes")
    if choice == "Y":
        service.save()
        print("Event records successfully saved!")
    else:
        start()
    choice = option("Would you like to add more service")
    if choice == "Y":
        services()
    else:
        adminMenuArgs()

def menuselect():
    menu()
    try:
        args = int(raw_input("PLEASE CHOOSE YOUR OPTION: "))
        check(args)
    except ValueError:
        print("\n")
        print("ERROR! PLEASE CHOOSE THE CORRECT OPTION FROM THE MENU!")
        menu()

# Menu for user type
def userMenu():
    print("----------------------")
    print("What can we do for you ?")
    print("1. REGISTER")
    print("2. VIEW BOOKING")
    print("3. EXIT")
    print("----------------------")

 # args for user menu
def userMenuSelection(args):
    if args == 1:
        register()
    elif args == 2:
        userViewBooking()
        menuselect()
    elif args == 3:
        exit()

def userViewBooking():
    userVoucher = int(raw_input("Voucher ID: "))
    Booking.printSingleRecord(userVoucher)

def start():
    choose()
    try:
        args = int(raw_input("PLEASE CHOOSE USER TYPE: "))
        selection(args)
    except ValueError:
        print("\n")
        print("ERROR! PLEASE CHOOSE THE CORRECT OPTION FROM THE MENU!")
        choose()

start()

