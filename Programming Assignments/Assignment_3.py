print("This is a file analyzer thingy.")
import string
from datetime import date
import os

textfile_input = input("Give a file name, make sure it has no quotes ")
if textfile_input == "":
    textfile_input = "../text_files/testing_text"
    with open(textfile_input, "r") as textfile_thing:
        original_textfile = textfile_thing.read()
else:
    try:
        with open(textfile_input, "r") as textfile_thing:
            original_textfile = textfile_thing.read()
    except (FileNotFoundError , OSError):
        print("File not found, check for spelling or case errors and check its in the right folder (if you used relative pathing), possibly if you have \" on either side it breaks.")
        exit()
word = input("What word do you want to search for (case-insensitive)").lower()
your_name = "Daryn"
your_full_name ="Daryn Collins"
quote = "Florpy Lorpy Lorp"

normalized_text = original_textfile.lower().translate(str.maketrans('', '', string.punctuation))
word_list = normalized_text.split()
wordvariable_count = word_list.count(word)
print(f"The word '{word}' appears {wordvariable_count} times in the file.")

char_count = len(original_textfile)
print(f"This has '{char_count}' characters (including spaces(i think lol))")

line_count = original_textfile.count("\n")+1
print(f"This has '{line_count}' lines")

name_count = word_list.count(your_name.lower())
print(f"My name is '{your_name}' it appears '{name_count}' times")

modified_text2 = original_textfile.replace("\n", " ").replace("\t", " ")
word_count_by_transition = 0
for i in range(1, len(modified_text2)):
    if modified_text2[i-1] == " " and modified_text2[i] != " ":
        word_count_by_transition += 1
if modified_text2 and modified_text2[0] != " ":
    word_count_by_transition += 1

print(f"This has '{word_count_by_transition}' words (counted efficiently trust)")

print("By teh way imma make a new file with some modifications")
folder_path, filename_only = os.path.split(textfile_input)
ext_index = filename_only.rfind(".")

if ext_index != -1:
    base = filename_only[:ext_index]
    ext = filename_only[ext_index:]
else:
    base = filename_only
    ext = ".txt"

makecopyfile_formod = os.path.join(folder_path, f"{base}_EDITED_BY_DC_{date.today()}{ext}")

# start with original and apply transformations step by step
transformed_text = original_textfile.upper()
transformed_text = transformed_text.replace(word.upper(), your_name)
transformed_text = transformed_text + f"\n{your_full_name} {quote}"
transformed_text = transformed_text.upper()
transformed_text = transformed_text.replace("A", "").replace("O","").replace("E", "").replace("P", "9")

with open(makecopyfile_formod, "w") as perma_mod:
    perma_mod.write(transformed_text)
