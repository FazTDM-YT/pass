import itertools as it
import random


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


## Welcoming
print(
    bcolors.OKBLUE
    + "Welcome to the Password Generator. This project was made by Faizan Ahmed"
)
print()
print(bcolors.OKBLUE + "Starting Password Generator...")
print("")

characters = {
    "Uppercases": ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"],
    "Lowercases": ["abcdefghijklmnopqyrstuvwxyz"],
    "Numbers": ["0123456789"],
    "Symbols": ["!@#$&*?_-+"],
}

while True:
    try:
        n = int(input("\tLength of Password: "))
        break
    except ValueError:
        print(bcolors.FAIL + "Entered Value should be integer only")
        print("Restarting the program...")
        print(bcolors.OKBLUE + "")
        pass


def gen_pass(n):
    print(bcolors.OKGREEN + "Select Character type number from the list: ")
    arr = ["Numbers", "Uppercases", "Lowercases", "Symbols"]
    l1 = list(it.combinations(arr, 1))
    l2 = list(it.combinations(arr, 2))
    l3 = list(it.combinations(arr, 3))
    l4 = list(it.combinations(arr, 4))
    l = l1 + l2 + l3 + l4  # list of all the possible combinations of characters
    for i in range(len(l)):
        print("\t", i + 1, " --- ", l[i])
    print(bcolors.OKBLUE + "")
    while True:
        c_type = int(
            input("Type any serial number from the above list of combinations: ")
        )
        if c_type in range(1, 16):
            break
        else:
            print(bcolors.HEADER + "Serial number should be from 1 to 15...")
            print(bcolors.OKBLUE + "")

    ## Generating password with selected combination
    s_comb_l = [i for i in list(l[c_type - 1])]  # selected character combination list
    print(s_comb_l)
    c_per_pass = n // len(s_comb_l)
    extra_c = n - (c_per_pass * len(s_comb_l))
    password_l = []
    all_char = []
    for i in range(0, len(s_comb_l)):
        x = s_comb_l[i]
        z = characters[x][0]
        l = [char for char in z]
        all_char.extend(l)
        c = random.choices(l, k=c_per_pass)
        password_l.extend(c)
    e_c = random.choices(all_char, k=extra_c)
    password_l.extend(e_c)
    random.shuffle(password_l)
    password = "".join(password_l)
    print(bcolors.HEADER + "Your password:", password)
    print(
        bcolors.OKCYAN
        + "To copy your password, hightlight the password and right click. Then click the copy option. Replit's Terminal does not support Ctrl C."
    )


gen_pass(n)


def hye():
    import secrets
    import string

    def generate_password(length, options, custom_words=None, min_requirements=None):
        chars = ""
        if "uppercase" in options:
            chars += string.ascii_uppercase
        if "lowercase" in options:
            chars += string.ascii_lowercase
        if "digits" in options:
            chars += string.digits
        if "special" in options:
            chars += string.punctuation

        password = ""
        if min_requirements:
            for req_type, req_count in min_requirements.items():
                req_chars = "".join(secrets.choice(chars) for _ in range(req_count))
                password += req_chars
                chars = chars.replace(req_chars, "")

        remaining_length = length - len(password)
        password += "".join(secrets.choice(chars) for _ in range(remaining_length))

        if custom_words:
            word_count = len(custom_words)
            split_length = length // word_count
            split_remainder = length % word_count

            for i, word in enumerate(custom_words):
                split_length += 1 if i < split_remainder else 0
                insert_index = secrets.randbelow(split_length - len(word) + 1)
                password = (
                    password[:insert_index]
                    + word
                    + password[insert_index + len(word) :]
                )
                split_length = length // word_count
                split_length = length // word_count

        password = "".join(secrets.choice(password) for _ in range(length))
        return password

    # Getting user preferences for password generation
    length = int(input("Enter the length of the password: "))
    print("Select the options for password generation (separated by a comma):")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Digits")
    print("4. Special characters")
    options_input = input("Enter the option numbers: ")
    options_list = options_input.split(",")

    # Mapping option numbers to option names
    options = []
    for option in options_list:
        if option == "1":
            options.append("uppercase")
        elif option == "2":
            options.append("lowercase")
        elif option == "3":
            options.append("digits")
        elif option == "4":
            options.append("special")

    # Getting custom word input from the user
    custom_words_input = input(
        "Enter custom words to include in the password (separated by a comma): "
    )
    custom_words = custom_words_input.split(",")

    # Getting minimum requirements for each character type
    min_requirements = {}
    for option in options:
        min_count = int(
            input(f"Enter the minimum number of {option} characters in the password: ")
        )
        min_requirements[option] = min_count

    # Generating the password
    password = generate_password(length, options, custom_words, min_requirements)

    # Displaying the generated password
    print("\n" + "=" * 20 + " Made by Faizan Ahmed " + "=" * 20)
    print("Generated Password:", password)
    print("=" * 56)


yes = input(
    """--------------------------------------------------------------
Do you want to use the beta version of the Password Generator
To answer put either
1 for Yes
2 for No
Input: """
)

if yes == "Yes" or yes == "1" or yes == "y" or yes == "yes" or yes == "YES":
    print("--------------------------------------------------------------")
    hye()
elif yes == "No" or yes == "2" or yes == "n" or yes == "no" or yes == "NO":
    print(
        bcolors.OKBLUE
        + "Bye, hope you had a good experience, if not please comment about it."
    )
else:
    print(
        bcolors.HEADER + "Error occured, please enter the correct responce next time."
    )
