import random


def main():
    import string
    print("this is a password generator btw")
    while True:
        try:
            passcount = int(input("How many passwords do you want?"))
            break
        except ValueError:
            print("Not a valid number")
    passwordlist = ""
    options = {
        "lowercase letters": string.ascii_lowercase,
        "uppercase letters": string.ascii_uppercase,
        "digits": string.digits,
        "special characters": string.punctuation
    }
    if passcount == 0:
        print("Then why are you even here?")
        exit()
    elif passcount <= 0:
        print("bro i cant make negative passwords but good job on finding an \"easter egg\" ig")
        exit()
    for i in range(passcount):
        it_works = False
        char_pool = []
        while True:
            try:
                charcount = int(input("How many characters do you want?"))
                break
            except ValueError:
                print("Not a valid number")
        for list_name, characters in options.items():
            response = input(f"Do you want {list_name} in your pool? ").lower()
            if response == "yes" or response == "":
                char_pool += list(characters)
        if char_pool == [] or charcount <= 0:
            print("I can't make a password out of nothing im just going to skip this one")
        else:
            try:
                currentpass = ''.join(random.choices(char_pool, k=charcount))
                it_works = True
            except:
                print("Sorry, this password didn't work probably too large or something similar.")
            if it_works == True:
                print(currentpass)
                passwordlist = passwordlist +currentpass + "\n"
    if it_works == True:
        passfolderquestion = input("Do you want this to be in a file (separated into different lines)?").lower()
        if passfolderquestion == "yes" or passfolderquestion == "":
            with open("../text_files/random_passwords.txt", "w") as file:
                file.write(passwordlist)

if __name__ == "__main__":
    main()