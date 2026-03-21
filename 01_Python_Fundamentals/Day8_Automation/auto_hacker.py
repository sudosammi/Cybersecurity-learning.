import os 
import time 

print("---AUTOMATION START---")

current_dir = os.getcwd()

print("Hum abhi yanah hai :  " , current_dir)

print("Creating 'Secret_Mission' folder...")
try:
    os.mkdir("Secret_Mission")
    print("Success: Folder Ban Gya!")

except FileExistsError:
    
    print("Notice: Folder Pahle se exist karta hai. (Skipping...) ")



time.sleep(1)

files = os.listdir()

print("Files in this folder:" , files)

print("---MISSION COMPLETE---")

	


