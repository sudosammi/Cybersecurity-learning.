#Simulated Server Login

database = {
	"saurabh" : "python_king",
	"guest" : "guest123"
}

print(" SECURE LOGIN SYSTEM ")
 
user = input("Username: ")

password = input("Password: ")

if user in database:
    if database[user] == password:
        print(" ACCESS GRANTED! Welcome Back..")

    else: 
        print("WRONG PASSWORD! Aleart sent to admin")
else:
    print("USER NOT FOUND")
