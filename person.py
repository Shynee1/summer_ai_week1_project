from queue import Queue

class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.description = f"Hello! My name is {name} and I am {age} years old."
        self.friendlist = []
        self.messages = Queue()
        
    def add_friend(self, person):
        self.friendlist.append(person)
        person.friendlist.append(self)
        print("Added " + person.id + " to friend list.")
        pass

    def remove_friend(self, person):
        self.friendlist.remove(person)
        person.friendlist.remove(self)
        print("Removed " + person.id + " from friends list.")
        pass

    def update_description(self):
        newDesc = input("\nEnter new description: ")
        self.description = newDesc
        print("Description updated. New description: " + self.description)
        pass

    def update_name(self):
        newName = input("\nEnter your new name: ")
        self.id = newName
        print("Name updated. New name: " + self.id)
        pass

    def send_message(self, person):
        message = input("\nEnter message: ")
        person.recieve_message(self, message)
        pass

    def recieve_message(self, person, message):
        formatted = person.id + ": " + message
        self.messages.put(formatted)
        pass

    def list_all_messages(self):
        if self.messages.empty():
            print("\nThere are no available messages.")
        else:
            print("\nMessages:")
            while not self.messages.empty():
                print(self.messages.get())
            print("********************************************************")
        pass

    def list_all_friends(self):
        if len(self.friendlist) == 0:
            print("\nYou have no friends.")
        else:
            print("\nFriends:")
            for person in self.friendlist:
                print(person.id)
            print("********************************************************")   
        pass
        
            
