


while True:
        userName = raw_input("Username: ")
        password = raw_input("Password: ")
        if userName == 'elmo' and password == 'blue':
                #let them in
                break #they are in, exit loop
        else:
                print("username or password inavlid!")
                print("Do you want to try again?")
                choice = raw_input("(Y)es or (N)o")
                print()
                if (choice == "y") or (choice == "Y"):
                    continue
                else:
                    break



