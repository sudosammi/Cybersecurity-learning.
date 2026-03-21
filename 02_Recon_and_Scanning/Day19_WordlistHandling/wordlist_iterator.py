file_name = "pass.txt"

try: 
    with open (file_name, "r") as file:
        print(f"[*] Opening wordlist: {file_name}")

        for line in file:
            password = line.strip()
            print(f"[!] Testing: {password}")

except FileNotFoundError:
    print("[X] Error: Creat 'pass.txt' first!")


