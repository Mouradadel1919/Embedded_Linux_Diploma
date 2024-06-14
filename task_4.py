letters = ["a", "e", "i", "o", "u"]

letter = str(input("Please Enter a letter: "))
for itr in letters:
    if letter == itr or (letter == itr.capitalize()):
        found = True
        break
    else:
        found = False

if found == True :
    print("Found It")

else:
    print("Not Found")
