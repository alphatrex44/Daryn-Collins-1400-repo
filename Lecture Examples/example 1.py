username=input("Please give your name: ")
it_works = False
while it_works == False:
    try:
        pennies = int(input("How many pennies do you have?: "))
        it_works = True
    except ValueError:
        print("That is not a whole digit!")
it_works = False
while it_works == False:
    try:
        nickels = int(input("How many nickels do you have?: "))
        it_works = True
    except ValueError:
        print("That is not a whole digit!")
it_works = False
while it_works == False:
    try:
        dimes = int(input("How many dimes do you have?: "))
        it_works = True
    except ValueError:
        print("That is not a whole digit!")
it_works = False
while it_works == False:
    try:
        quarters = int(input("How many quarters do you have?: "))
        it_works = True
    except ValueError:
        print("That is not a whole digit!")
change = float(((pennies+(nickels*5)+(dimes*10)+(quarters*25))/100))
print("Hello "+ username+", you have $"+(str(change))+" in change.")

