import re
import random 
import string
import math
import getpass

from colorama import Fore, Style, init

init()

password = getpass.getpass("Enter a password to analyze(hidden):")

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    return score, suggestions



def get_strength_level(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"



def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset) if charset > 0 else 0
    return entropy

def improvement_suggestions(password):
    suggestions = []

    if not any(c.islower() for c in password):
        suggestions.append("Add lowercase letters")
    if not any(c.isupper() for c in password):
        suggestions.append("Add uppercase letters")
    if not any(c.isdigit() for c in password):
        suggestions.append("Add numbers")
    if not any(c in "!@#$%^&*()-_=+[]{}|;:',.<>?/" for c in password):
        suggestions.append("Add symbols")
    if len(password) < 12:
        suggestions.append("Increase password length to 12 or more characters")

    return suggestions

def main():
    print("1. Analyze a password")
    print("2. Generate a secure password")

    choice = input("Choose an option (1 or 2): ")

    if choice == "1":
        password = input("Enter a password to analyze: ")

        score, suggestions = check_password_strength(password)
        strength = get_strength_level(score)

        entropy = calculate_entropy(password)
        print("Password Entropy:", round(entropy,2), "bits")

     
    if strength == "Weak":
        print(Fore.RED + "\nPassword Strength: Weak" + Style.RESET_ALL)
    elif strength == "Medium":
        print(Fore.YELLOW + "\nPassword Strength: Medium" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "\nPassword Strength: Strong" + Style.RESET_ALL)

    if suggestions:
        print("\nSuggestions to improve:")
        for s in suggestions:
            print("-", s)

    elif choice == "2":
        length = int(input("Enter password length: "))
        password = generate_password(length)

        print("\nGenerated Secure Password:", password)

    

if __name__ == "__main__":
    main()
