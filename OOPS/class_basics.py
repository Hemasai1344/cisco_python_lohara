class Dog:
    # Class attribute
    species = "Canis lupus familiaris"
    
    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating an object (instance of the class)
dog1 = Dog("Charlie", 3)
print(dog1.description())  # Output: Buddy is 3 years old.
print(dog1.speak("Woof!\n"))  # Output: Buddy says Woof!

dog2 = Dog("Chimtu",2)
print(dog2.description())
print(dog2.speak("Namaste Bhai\n"))

dog3 = Dog("Chinnu",1)
print(dog3.description())
print(dog3.speak("Chai Chai\n"))


dogs=[dog1, dog2, dog3]

#map
#filter
#aggregator function like reduce

from functools import reduce
#reduce syntax
# reduce((function),dogs,0)
ages_sum = reduce((lambda s,dog: s+dog.age), dogs, 0)
print(ages_sum)

lst = [10,20,30,41]
nums_sum = reduce(lambda s,i: s+i, lst, 0)
nums_product = reduce(lambda p,i: p*i, lst, 1)
print(nums_sum, nums_product)