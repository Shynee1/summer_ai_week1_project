# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create account")
    print("2. Login")
    print("3. Account details")
    print("4. Messages")
    print("5. Friends")
    print("6. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my name")
    print("2. Edit my description")
    print("3. <- Go back ")
    return input("Please Choose a number: ")

def manageFriends():
    print("")
    print("1. Add a friend")
    print("2. Remove a friend")
    print("3. View all my friends")
    print("4. <- Go back ")
    return input("Please Choose a number: ")

def manageMessages():
    print("")
    print("1. Send a message")
    print("2. View all my messages")
    print("3. <- Go back ")
    return input("Please Choose a number: ")
