# Constructor of human class
# init function in blid
# class Human:
#     def __init__(self, name, age , gender): # Constructor of human class
#         self.name = name
#         self.age = age
#         self.gender = gender



class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


# Create an object
person = Human("Alice", 25)

# Access the object's methods and attributes
person.speak()  


