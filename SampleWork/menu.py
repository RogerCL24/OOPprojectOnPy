class MainMenu:

    @staticmethod
    def showMainMenu():
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("          TDD-INC - PYTHON CONTACTS        ")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("1. Add contact")
        print("2. List contacts")
        print("3. Search contact")
        print("4. Edit contact")
        print("5. Close app")
        opt = int(input("Select an option please: "))
        print("\n")
        while opt > 5 or     opt < 1:
            print(f"\n    Option {opt} is not valid \n")
            opt = int(input("Select an option please: "))
        else:
            return opt

    @staticmethod  
    def showMenuAddContact():
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("                 ADD CONTACT                   ")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    @staticmethod
    def addContact():
        name = input("Write the name: ")
        email = input("Write the mail: ")
        phone = input("Write the phone: ")
        return name, email, phone
    
    @staticmethod
    def showlistAllContacts():
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("              CONTACT LIST                     ")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("Name     |       Mail     |      Phone         ")

    @staticmethod
    def showMenuSearchContact():
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("              SEARCH CONTACT                   ")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    @staticmethod
    def searchContact():
        return input("Write the mail you want to search: ")
    
    @staticmethod
    def showMenuUpdate():
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("              UPDATE MENU                      ")

    @staticmethod
    def getContactEmail():
        return input("Write contact mail: ")
    
    def getContactData():
        name = input("Write the contact name: ")
        phone = input("Write the contact phone number: ")
        return name, phone