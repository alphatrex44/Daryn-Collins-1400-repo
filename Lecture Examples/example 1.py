username=input("Please give your name: ")
#i make it works false every time so the loop will always work again
it_works = False
#this makes so if you dont do an integer it tells you to do a whole number then lets you input again
while it_works == False:
    try:
        pennies = int(input("How many pennies do you have?: "))
        it_works = True
    except ValueError:
        print("That is not a whole digit!")
it_works = False
#i know i could use functions but idk how to use parameters so i dont use function
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
#this is to capitalize the username
username=username.capitalize()
#this is to calculate the change and avoid string+float errors
change = float(((pennies+(nickels*5)+(dimes*10)+(quarters*25))/100))
#prints the stuff
print("Hello "+ username+", you have $"+(str(change))+" in change.")

