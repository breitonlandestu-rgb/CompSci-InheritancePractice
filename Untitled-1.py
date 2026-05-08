



class Vehicle:

    def __init__(self, make, model):

        self.make = make
        self.model = model

def start(self):

    return f"{self.make} {self.model} starting..."

class Car(Vehicle):

    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

def start(self):

    base = super().start()

    return f"{base} vroom!"

# Create and use the car
my_car = Car("Toyota", "Corolla", 4)
print(my_car.start())