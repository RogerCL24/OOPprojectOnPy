
class User:
    def __init__(self, name, lastname, password, mail, phone):
        # Public atributes
        self.name = name
        self.lastname = lastname 
        self.mail = mail
        # Private atributes
        self.__password = password
        self.__phone = phone

    def printPhoneNum(self, password):
        if password == self.__password:
            print(self.__phone)
        else:
            print("Sorry, wrong password")

    def getPhoneNum(self):
        return self.__phone

    def updatePhoneNum(self, phone_num):
        self.__phone = phone_num

    def encryptPassword(self, password):
        pass
    
    def verifyPassword(self, password):
        pass 


user1 = User(
    name= "Roger",
    lastname= "Cot",
    password= "1234",
    mail= "roger@gmail.com",
    phone= "78789051"
)
user1.printPhoneNum(input("Write your password please: "))
user1.updatePhoneNum(786761)
user1.printPhoneNum(input("Write your password please: "))