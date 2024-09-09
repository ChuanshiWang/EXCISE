# 1. Ask user to enter a string and check that it is made up only of alphabets:

def check_only_alphabets():
    while True:
        user_input = input("Enter a string: ")
        if user_input.isalpha():
            print("Valid string with only alphabets!")
            break
        else:
            print("Invalid input. The string should only contain alphabets.")

check_only_alphabets()
# 2. Now, make sure that the string is made up of both alphabets and numbers:

def check_alphanumeric():
    while True:
        user_input = input("Enter a string with both alphabets and numbers: ")
        if user_input.isalnum():
            print("Valid alphanumeric string!")
            break
        else:
            print("Invalid input. The string should contain only alphabets and numbers.")

check_alphanumeric()
# 3. Now, make sure that the string is made up of both alphabets and at least one number:

def check_alpha_and_digit():
    while True:
        user_input = input("Enter a string with both alphabets and at least one number: ")
        if any(char.isalpha() for char in user_input) and any(char.isdigit() for char in user_input):
            print("Valid string with alphabets and at least one number!")
            break
        else:
            print("Invalid input. The string should contain both alphabets and at least one number.")

check_alpha_and_digit()
# 4. Now, make sure that the string is made up of both alphabets, at least one number, and at least one special character:

def check_alpha_digit_special():
    while True:
        user_input = input("Enter a string with alphabets, at least one number, and one special character: ")
        if (any(char.isalpha() for char in user_input) and
                any(char.isdigit() for char in user_input) and
                any(not char.isalnum() for char in user_input)):
            print("Valid string with alphabets, numbers, and a special character!")
            break
        else:
            print("Invalid input. The string should contain alphabets, numbers, and at least one special character.")

check_alpha_digit_special()
# 5. Now, modify the above code so that if the user enters an invalid string,
# the program should ask the user to enter another string again, and keep asking until a valid string has been entered:

def validate_string():
    while True:
        user_input = input("Enter a valid string (alphabets, at least one number, and one special character): ")
        if (any(char.isalpha() for char in user_input) and
                any(char.isdigit() for char in user_input) and
                any(not char.isalnum() for char in user_input)):
            print("Valid string entered!")
            break
        else:
            print("Invalid input. Please try again.")

validate_string()