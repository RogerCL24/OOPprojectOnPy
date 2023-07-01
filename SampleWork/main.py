from contacts import Contacts
from menu import MainMenu
import os

if __name__ == '__main__':
    os.system("clear")
    while True:             # OBS: if you have 3.10 python vers or newer you can use match
        opt = MainMenu.showMainMenu()
        contacts = Contacts()
        if opt == 1:  # Add contact  
            MainMenu.showMenuAddContact()
            name, email, phone = MainMenu.addContact()
            contacts.add(name, email, phone)
            os.system("clear")
        elif opt == 2:  # List contacts
            os.system("clear")
            MainMenu.showlistAllContacts()
            contacts.show_all_contacts()
            print("\n")
        elif opt == 3:  # Search contacts
            os.system("clear")
            MainMenu.showMenuSearchContact()
            mail = MainMenu.searchContact()
            contact = contacts.search(mail)
            if contact:
                print("\n")
                print(contact)
                print("\n")
            else:
                print("\n    Not found \n")  

        elif opt == 4:  # Edit contacts
            os.system("clear")
            MainMenu.showMenuUpdate()
            MainMenu.showlistAllContacts()
            contacts.show_all_contacts()
            mail = MainMenu.searchContact()
            contact = contacts.search(mail)
            if contact != None:
                name, phone = MainMenu.getContactData()
                resp = contacts.update(contact["email"],name, phone)
                print("Contact updated")
            else:
                print("\n    Not found \n") 

        elif opt == 5:           # Close app
            os.system("clear")
            print("Signing out...")
            break
