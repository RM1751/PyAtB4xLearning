#### # Public : Variable - Don't Mention anything
#Members are accessible from anywhere in the program.
#### # Protected : _
#Members are intended for internal use within the class and its subclasses.

#### # Private : __
# Members are only accessible within the class they are defined in.





class My_Class:
    # public variable
    public_var = "I am puublic" # instance variable
    balance = "100"
    # private variable
    __private_var = "I am private"
    __password = "123"
    # protecteed variable
    _protected = "I am protected"


obj = My_Class()
print(obj.public_var)
print(obj.balance)
print(obj._protected)

print(obj.private_var)
print(obj.__password)
