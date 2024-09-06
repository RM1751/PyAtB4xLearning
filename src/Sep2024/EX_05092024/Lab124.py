"""Python Inheritance
Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class."""


class Father:
    key = "2 bhk "

    def car(self):
        print("This is fatner car")


class son(Father):
    pass


father_obj = Father()
father_obj.car()
son_obj = son()
son_obj.car()
