class Person:
    def __init__(self):
        self.name = input("Enter The name \n")
        self.age = int(input("Enter the age \n"))
        self.phone = input("Enter the phone \n")
        self.occupation = input("Enter the occupation \n")

    def display_information(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"phone is {self.phone}")
        print(f"occupation is {self.occupation}")


# create a object
person1 = Person()

# function call
person1.display_information()
