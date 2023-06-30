from cryptocode import encrypt, decrypt
from abc import ABC, abstractmethod

class BaseUser(ABC):
    
    def __init__(self, name, lastname, mail, password, phone_num):
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = self.encryptPassword(password)
        self.phone_num = phone_num

    @abstractmethod
    def encryptPassword(self, password):
        pass
    
    @abstractmethod
    def verifyPassword(self, password):
        pass


class ParticularUser(BaseUser):

    def encryptPassword(self, password):
        return encrypt(password, "secret")
    
    def verifyPassword(self, password):
        decryptedPass = decrypt(self.password, "secret")
        return decryptedPass == password
    
user1 = ParticularUser(
    name = "Roger",
    lastname = "Cot",
    mail = "roger@gmail.com",
    password = "1234",
    phone_num = "78789152"
)

print(user1.password)
print(user1.verifyPassword("1234"))
