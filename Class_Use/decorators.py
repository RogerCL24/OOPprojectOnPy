
class MyClass:
    def __init__(self, color):
        self.color = color
    
    @staticmethod      # Acces to attributes is not allowed
    def static_method(color):   # It is not the attribute!
        print(f"This is an static method with color {color}")
    
    @classmethod       # Open acces to all attributes and methods
    def class_method(cls):
        print("This is a class method...")

myclass = MyClass("Red")
MyClass.static_method("Black")