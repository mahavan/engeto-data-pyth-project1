# Project 1: Text Analyzer

TEXTS = [
    """Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."""
]

users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
}

print("Welcome to the Text Analyzer!")
print("Enter your username and password.")

username = input("Username: ")
password = input("Password: ")
print("-" * 35)

if users.get(username) == password:
    print(f"Welcome {username}!")
    print(f"We have {len(TEXTS)} texts to be analyzed.")

    text_choice = input(
        f"Enter a number between 1 and {len(TEXTS)} to select a text: ")
    if not text_choice.isdigit():
        print("You must enter a number! Exiting the program.")
        exit()
    if not (1 <= int(text_choice) <= len(TEXTS)):
        print("Invalid text selection. Exiting the program.")
        exit()

    text = TEXTS[int(text_choice) - 1]
    words = text.split()
    title_words = [word for word in words if word.istitle()]
    uppercase_words = [word for word in words if word.isupper()]
    lowercase_words = [word for word in words if word.islower()]
    numeric_strings = [word for word in words if word.isdigit()]
    numeric_values = [int(word) for word in numeric_strings]
    
    print("-" * 35)
    print(f"There are {len(words)} words in the selected text.")
    print(f"There are {len(title_words)} titlecase words.")
    print(f"There are {len(uppercase_words)} uppercase words.")
    print(f"There are {len(lowercase_words)} lowercase words.")
    print(f"There are {len(numeric_strings)} numeric strings.")
    print(f"The sum of all the numbers {sum(numeric_values)}.")
    print("-" * 35)
    print("LEN |       OCCURRENCES       | NR.")
    print("-" * 35)

    word_length_counts = {}
    # Count occurrences of each word length
    for word in words:
        clean_word = word.strip(".,")
        length = len(clean_word)
        # If the key (length) does not exist, use the default value of 0
        word_length_counts[length] = word_length_counts.get(length, 0) + 1
    for length in sorted(word_length_counts):
        count = word_length_counts[length]
        print(f"{length:>3} | {'*' * count:<23} | {count}")

else:
    print("Unregistered user or incorrect password. Exiting the program.")
    exit()