
class User():
    # Data (attributes)
    # Constructor
    def __init__(self, na, la, ma, pa, ph):
        self.name = na
        self.lastname = la
        self.mail = ma
        self.password = pa
        self.phone_num = ph

    # funcionality (methods)
    def encryptPassword(self):
        pass

    def verifyPassword(self):
        pass


user1 = User(
    na="Roger",
    la="Cot", 
    ma="roger@gmail.com",
    pa="1234",
    ph="78789097"
)
print(user1.name + " " + user1.lastname)
