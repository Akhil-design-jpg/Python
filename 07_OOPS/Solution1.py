# Object oriented programming

# Car class with attributes like brand and model. Then create an instance of the class

class Car:
    def __init__(self, brand,model):
        self.brand = brand
        self.model = model

my_Car = Car("Toyota","Corolla") # my_Car is an object
print(my_Car.brand)
print(my_Car.model)
# self same as this in js 



my_new_car = Car("Tata","Safari")
print(my_new_car.model)