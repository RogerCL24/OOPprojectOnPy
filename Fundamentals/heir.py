
class Vehicle():
    # Atributes
    def __init__(self, speed, brand, model, year, passengers):

        self.passengers = passengers
        self.speed = speed
        self.brand = brand
        self.model = model
        self.year = year

    # Methods

    def accelerate(self, speed):
        self.speed += speed

    def brake(self, speed):
        self.speed -= speed


# Motorbike inherit Vehicle's functionalities
class Motorbike(Vehicle): 
    def __init__(self, speed, brand, model, passengers, year, motor):
        super().__init__(brand, speed, model, year, passengers)     # Update base class atributes
        self.motor = motor
    
    def wheelie(self):
        return "You almost fall over, but there you are doing a wheelie"

class Bus(Vehicle):
    
    def __init__(self, speed, brand, model, year, passengers, seats):
        super().__init__(speed, brand, model, year, passengers)
        self.seats = seats

    def loadPassengers(self, passengers):
        self.passengers += passengers
        return f"passengers on board: {passengers}"

    def downloadPassengers(self, passengers):
        self.passengers -= passengers
        return f"step down carefully: {passengers}"

vehicle1 = Motorbike (
    speed= 30,
    brand= "Suzuki",
    model= "Hayabusa 1300",
    passengers= 1,
    year= 2010,
    motor= 1340
)

print(vehicle1.wheelie())