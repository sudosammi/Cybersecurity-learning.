#DAY 9 : Spy diary - Writing

print("---CLASSIFIDE TERMINAL---")

file = open("secret.txt" , "a")

data = input("Enter ypur secret mission: ")

file.write("LOG ENTRY: " + data + "\n" )

file.close()

print("Secret ADDED to logs. " )


