from  person import Person
from social_network import SocialNetwork
import social_network_ui

#Create instance of main social network object
ai_social_network = SocialNetwork()

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            ai_social_network.create_account()

        elif choice == "2":
            ai_social_network.login()

        elif choice == "3":
            ai_social_network.manage_account()
        
        elif choice == "4":
            ai_social_network.manage_messages()

        elif choice == "5":
            ai_social_network.manage_friends()

        elif choice == "6":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
