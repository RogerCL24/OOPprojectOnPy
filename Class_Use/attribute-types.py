class Vehicle():
    # Class attribute
    wheel_num = 4

    # Instance attribute
    def __init__(self, speed, brand, model, year, passengers):

        self.passengers = passengers
        self.speed = speed
        self.brand = brand
        self.model = model
        self.year = year



    def accelerate(self, speed):
        self.speed += speed

    def brake(self, speed):
        self.speed -= speed

vehicle1 = Vehicle(
    speed= "30",
    brand= "nissan",
    model= 300,
    year= 2020,
    passengers= 2
)

print(vehicle1.wheel_num)
print(vehicle1.brand)
print(vehicle1.model)
print(vehicle1.speed)

Vehicle.wheel_num = 6 # if you want to change only 1 instance then, -> vehicle1.wheel_num = 6

print(vehicle1.wheel_num)

# Data attribute
vehicle1.color = "red" # Only the vehicle1 instance has this attribute
print(vehicle1.color)