class Check_Balance(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(msg)


balance = 1000
withdraw =int(input("Enter amount to withdraw "))
if withdraw > balance:
    raise Check_Balance("balance is low ")
else:
    print("you have withdraw", withdraw,  "Reaming bal", (balance - withdraw))
