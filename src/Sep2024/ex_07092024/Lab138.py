# Method Overloading:
# Python does not support method overloading
# in the traditional sense.

class MathUtils(object):  # is- A object - single inheritnace
    # Method - overloading - Not supported!
    # def add(self, a, b):
    #     return a + b
    #
    # def add(self, a, b, c):
    #     return a + b + c

    def add(self, a, b, c):
        return a + b + c


math = MathUtils()
op1 = math.add(1, 2,4)
print(op1)