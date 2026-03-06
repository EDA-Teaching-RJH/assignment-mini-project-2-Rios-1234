
def main():
    # Create a PasswordChecker instance that will handle:
    # - rule checking
    # - scoring
    # - strength labeling
    # - saving/viewing history
    checker = PasswordChecker()

    # Main program loop — keeps running until the user chooses to quit
    while True:
        print("\nPassword Checker Menu")
        print("1. Check a password")
        print("2. View password history")
        print("3. Quit")

        # Get the user's menu choice
        choice = input("Choose an option (1-3): ")
