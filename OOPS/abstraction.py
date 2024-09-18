from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car starts."

class Bike(Vehicle):
    def start(self):
        return "Bike starts."
#vehi = Vehicle() #TypeError: Can't inistantiate abstract class Vehicle with abstract method start
car = Car()
bike = Bike()
print(car.start())  # Output: Car starts.
print(bike.start())  # Output: Bike starts.