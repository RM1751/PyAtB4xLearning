# Class and Object Assignment
#
#
# Create a Employee Class
# A - name,age, phone, address, eid
# B - walk, talk, printdetails,
# with the Constructor which will set the values
# Ask the user about the information for E1, E2
# print the details of the E1, E2 via the print employee functions.
import none


class Employee:
    name = None
    age = None
    number = None
    address = None
    eid = None
    phone = None

    def __init__(self, name, age, number, address, eid):
        self.name = name
        self.age = age
        self.number = number
        self.address = address
        self.eid = eid

    def talk(self):
        print("Employee " + self.name + " is talking")
        return None

    def walk(self):
        print("Employee " + self.name + " is walking")
        return None


def walk(self):
    print("Employee " + self.name + " is walking")
    return None


def talk(self):
    print("Employee " + self.name + " is talking")
    return None


n = input("Enter the employee name\n")
a = input("Enter the employee age\n")
p = input("Enter the employee phone number\n")
ad = input("Enter the employee address\n")
e = input("Enter the employee eid\n")

employee1 = Employee(n, a, p, ad, e)
print("Employee details: \n", "Name: ", employee1.name, "Age: ", employee1.age, "Phone: ", employee1.phone, "Address: ", employee1.address,
      "EID: ", employee1.eid)
print(employee1)
print(employee1.name)
employee1.walk()
employee1.talk()
