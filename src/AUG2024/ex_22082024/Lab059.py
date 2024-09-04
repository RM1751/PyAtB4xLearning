from unittest import case

user_type = input("Enter user type\n")
match user_type:
    case "admin"| "manager":
        print("Hello admin")
    case "guest":
        print("hello guest")
    case _:
        print("you r nothing")


