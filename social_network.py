from person import Person
import social_network_ui

# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = []
        self.primary_account = None

    def get_user(self, name):
        for u in self.list_of_people:
            if u.id == name:
                return u

        return None
    
    def login(self):
        name = input("\nEnter username: ")
        user = self.get_user(name)
        if user == None:
            print("This account does not exist.")
            return
        self.primary_account = user
        pass

    def create_account(self):
        while True:
            name = input("\nAccount name: ")
            if name in self.list_of_people:
                print("Name is already taken.")
                continue

            age = input("Age: ")
            if not age.isnumeric():
                print("Enter a valid age.")
                continue

            person = Person(name, age)
            self.list_of_people.append(person)
            self.primary_account = person

            print("Account created!")
            break
        pass

    def manage_account(self):
        choice = social_network_ui.manageAccountMenu()
        while True:
            if choice == "1":
                self.primary_account.update_name()
                break
            elif choice == "2":
                self.primary_account.update_description()
                break
            elif choice == "3":
                break
            else:
                print("Not a valid option.")
        pass

    def manage_friends(self):
        choice = social_network_ui.manageFriends()
        while True:
            if choice == "1":
                fUsername = input("\nEnter friend username: ")
                fUser = self.get_user(fUsername)
                if fUser == None:
                    print("No user has this username.")
                    break
                self.primary_account.add_friend(fUser)
                break
            elif choice == "2":
                fUsername = input("\nEnter friend username: ")
                fUser = self.get_user(fUsername)
                if fUser == None:
                    print("No user has this username.")
                    break
                self.primary_account.remove_friend(fUser)
                break
            elif choice == "3":
                self.primary_account.list_all_friends()
                break
            elif choice == "4":
                break
        pass

    def manage_messages(self):
        choice = social_network_ui.manageMessages()
        while True:
            if choice == "1":
                fUsername = input("\nEnter username: ")
                fUser = self.get_user(fUsername)
                if fUser == None:
                    print("No user has this username.")
                    break
                self.primary_account.send_message(fUser)
                break
            elif choice == "2":
                self.primary_account.list_all_messages()
                break
            elif choice == "3":
                break
            else:
                print("Not a valid option.")
        pass
        
