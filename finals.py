import os
from user import User
from package import Package
from record import Record
# from booking import Booking

# validating the menu choices
def check(args):
    if args == 1:
        register()
    elif args == 2:
        createPackage()
    elif args == 3:
        bookTour()
    elif args == 4:
        checkBooking()
    elif args == 5:
        updateBooking()
    elif args == 6:
        cancelBooking()
    elif args == 7:
        check_db()
    elif args == 8:
        exit()

# menu for adding inclusions yes or no
def option(message):
    key = raw_input("{}? [Y]es/[N]o: " . format(message))
    return key

# displays the main menu
def menu():
    print("****************************")
    print("* 1. REGISTER CUSTOMER     *")
    print("* 2. CREATE EVENT          *")
    print("* 3. BOOK A TOUR           *")
    print("* 4. CHECK BOOKING         *")
    print("* 5. UPDATE BOOKING        *")
    print("* 6. CANCEL BOOKING        *")
    print("* 7. CHECK DB CONNECTION   *")
    print("* 8. EXIT                  *")
    print("****************************")

# registers customer
def register():
    os.system('clear')
    model = User()
    model.setFname(raw_input("First Name: "))
    model.setLname(raw_input("Last Name: "))
    model.setAddress(raw_input("Address: "))
    model.setContact(raw_input("Contact Number: "))
    model.setFullname()

    choice = option("Would you like to save changes")
    if choice == "Y":
        model.save()
        print("User records successfully saved!")
    else:
        start()
    choice = option("Would you like to register another user")
    if choice == "Y":
        register()
    else:
        start()


# create tour packages
def createPackage():
    os.system('clear')
    event = Package()
    event.setEventName(raw_input("Event Name: "))
    event.setLocation(raw_input("Event Location: "))
    event.setDuration(raw_input("Duration in Hrs: "))
    event.setRate(raw_input("Rate per Head: "))
    event.addInclusion(raw_input("Inclusion: "))

    # key = option("Would you like to add inclusions")
    # while key == "Y" or key == "y":
    #     event.addInclusion(raw_input("Inclusion: "))
    #     key = option("Would you like to add more inclusions")

    choice = option("Would you like to save changes")
    if choice == "Y":
        event.save()
        print("Event records successfully saved!")
    else:
        start()
    choice = option("Would you like to create another event")
    if choice == "Y":
        createPackage()
    else:
        start()

# book tour packages
def bookTour():
    print("book tour")

# check existing booking record
def checkBooking():
    # package = Package.getbyID(6)
    # print(package.event_name)
    #
    # user = User.getbyID(6)
    # print(user.full_name)

# update existing booking record
    User.printUserRecords()
def updateBooking():
    print("update booking")

# cancel existing booking record
def cancelBooking():
    print("cancel booking")

def check_db():
    Record.checkConnection()

    # initializes the program
def start():
    os.system('clear')
    menu()
    try:
        args = int(input("PLEASE CHOOSE YOUR OPTION: "))
        check(args)
    except ValueError:
        print("\n")
        print("ERROR! PLEASE CHOOSE THE CORRECT OPTION FROM THE MENU!")
        menu()

start()