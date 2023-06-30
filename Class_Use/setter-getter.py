class User:
    def __init__(self, name, lastname, password):
        self._name = name
        self._lastname = lastname
        self._password = password

    def encryptPassword(self, password):
        pass
    def verifyPassword(self, password):
        pass

    # Getter
    @property
    def name(self):
        return self._name
    
    # Setter
    @name.setter
    def name(self, name):
        self._name = name

    # Getter
    @property
    def lastname(self):
        return self._lastname
    
    # Setter
    @lastname.setter
    def lastname(self, lastname):
        self._lastname = lastname

user1 = User(
    name = "Roger",
    lastname = "Cot",
    password = "1234"
)
print(user1.name)
print(user1.lastname)
user1.name = "Arnau"
user1.lastname = "Lopez"
print(user1.name)
print(user1.lastname)
