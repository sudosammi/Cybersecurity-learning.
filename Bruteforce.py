import time 

print("---DICTIONARY ATTACK STARTED---")

correct_password = "saurabh123"

password_list = ["admin", "root", "12345", "password", "saurabh123", "god"]

for p in password_list:
    print("Trying password: " + p)
    time.sleep(0.5)

    if p == correct_password:
        print(" MATCH FOUND ! Password is: " +p)
        break

    else:
        print(" Failed... ")



print("---HACKING FINISHED---")
