class login:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def check_login(self):
        if self.email == "abc@gmail.com" and self.password == "123":
            print("User can login")
        else:
            print("user not register")


obj = login(email=input("Enter the email\n"), password=input("Enter the password\n"))
obj.check_login()
