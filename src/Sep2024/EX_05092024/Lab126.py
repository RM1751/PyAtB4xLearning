
# Multi Level Inheritance
class Grandfather:
    gold = " faher's 1kg gold "
    def flat(self):
        print("1 bhk")
class Father(Grandfather):
    diamand = " 2kg "
    def bhk2(self):
        print("Father have 2 bhk")
class Son(Father):
    btc = "1 btc"
    def bhk3(self):
        print("Son have 3 bhk")
s = Son()
f = Father()
G = Grandfather()
print(s.diamand)
print(s.gold)
print(f.gold)
#print(f.btc)
