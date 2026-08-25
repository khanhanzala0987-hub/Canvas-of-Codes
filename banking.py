
class Bank:

    def admin(self):
        print("Admin Login")
        admin = input("Enter admin id: ")
        password = input("Enter password: ")

        if admin == "admin" and password == "1234":
          print("1. Create Account")
          print("2. Delete Account")
          print("3. Renew Account")

    def user(self):
        print("User Login")
        user = input("Enter User id: ")
        pswd = input("Enter User password: ")

        if user == "user" and pswd == "4321":
            print("1. Show Bank Balance")
            print("2. Apply for Credit")
            print("3. Renew my Name")



hi = ("Enter 1 for Admin Login")
print(hi)
hii = ("Enter 2 for User Login") 
print(hii)

useranswer = input("Enter your Input: ")

b = Bank()

if useranswer == "1":
    b.admin()
elif useranswer == "2":
    b.user()
