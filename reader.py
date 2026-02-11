# DAY 9 : Spy reader

import time 

print("---ACCESSING SECURE FILE---")
time.sleep(1)

try: 
    file = open("secret.txt", "r")

    content = file.read()
    
    print("DECRYPTED MESSAGE FOUND")
    print("-----------------------")
    print(content)
    print("-----------------------")

    file.close()

except FileNotFoundError:    
    print("Error: 'secret.txt' file nahi mili! Kya tumne banayi hai ??")

