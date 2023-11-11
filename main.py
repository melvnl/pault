import json
import getpass
import pyperclip

def load_passwords_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            passwords = json.load(file)
        return passwords
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def get_user_password():
    entered_password = getpass.getpass("Enter the password: ")
    return entered_password

def print_passwords(passwords):
    print("+----------------------+----------------------+")
    print("| {:<20} | {:<20} |".format("Subject", "Masked Password"))
    print("+----------------------+----------------------+")

    for key, value in passwords.items():
        masked_password = '*' * len(value)
        print("| {:<20} | {:<20} |".format(key, masked_password))

    print("+----------------------+----------------------+")
    print()
    print()

def main():
    passwords = load_passwords_from_json("creds.json")

    entered_password = get_user_password()

    #Use your own desired password
    if entered_password == "":
        print("Password accepted. Choose a key to print the corresponding password:")
        print_passwords(passwords)

        user_key = input("Enter subject to retrieve password: ")
        if user_key in passwords:
            password_to_copy = passwords[user_key]
            pyperclip.copy(password_to_copy)

            print("The password for subject '{}' is copied to the clipboard.".format(user_key))
        else:
            print("subject '{}' not found.".format(user_key))
    else:
        print("Incorrect password. Exiting.")

if __name__ == "__main__":
    main()
