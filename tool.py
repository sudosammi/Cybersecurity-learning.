# Day 13: Using Modules (The Hacker's Way)

# 1. Modules ko import karna (Hathiyar uthana)
import os       # Operating System control
import random   # Random number generator
import time     # Time delays

# Screen saaf karna (Linux command 'clear' run karega)
os.system("clear")

print("--- 🕵️‍♂️ AUTO HACKER TOOL V2.0 ---")
time.sleep(1)

# List of targets (Hum computer se choose karwayenge)
targets = ["NASA", "Facebook", "Google", "Bank_Server", "Padosi_Ka_WiFi"]

# 2. Random module ka use (Koi ek target pick karo)
selected_target = random.choice(targets)

print("Target Lock kiya ja raha hai: " + selected_target)

# Thoda fake hacking feel (Random time delay)
wait_time = random.randint(1, 4)  # 1 se 4 second ke beech ka number
print("Encryption todne mein " + str(wait_time) + " seconds lagenge...")
time.sleep(wait_time)

print("✅ ACCESS GRANTED!")
print("---------------------------------")

# 3. OS Module ka asli use (System Info nikalna)
print("[*] Checking System IP Address...")
time.sleep(1)

# Ye Python ke andar se asli Linux command chala raha hai!
# 'ip a' command IP address dikhata hai
os.system("ip a") 

print("---------------------------------")
print("[*] Creating a fake virus file...")
# Linux command to create a file
os.system("touch virus.txt") 
print("File 'virus.txt' created successfully!")
