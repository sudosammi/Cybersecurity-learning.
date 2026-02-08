print("---PASSWORD CRACK TIME CALCULATOR---")

password = int(input("Total Password kitne hai : "))

speed = int(input("1 sec mai kitne try kr sakta hu : "))

seconds = password / speed

print("need:",seconds,"sec")


# ---YANHAN SE NAYA LOGIC HAI---

if seconds < 60:
    print("BOOM! bahut aasan hai . Attack kro!")

else:
    print("Bhai rahne dete hai Time lagega.")
