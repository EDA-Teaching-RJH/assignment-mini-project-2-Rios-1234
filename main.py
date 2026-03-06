
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
    if choice == "1":

            # Show the user what rules their password must meet
            print("\nYour password must meet ALL of these rules:")
            print("At least 8 characters long")
            print("At least one uppercase letter")
            print("At least one lowercase letter")
            print("At least one digit")
            print("At least one symbol")

            # Loop until the user enters a password that passes all rules
            while True:
                pwd_input = input("\nEnter a password: ")
                pwd = Password(pwd_input)

                # Run the password through the checker
                rules = checker.check(pwd)
                score = checker.score(rules)
                 # If all 5 rules pass, accept the password
                if score == 5:
                    print("\nPassword accepted!")
                    checker.pretty_print(rules)
                    break
                else:
                    # Show which rules failed so the user can fix them
                    print("\nPassword does NOT meet the requirements:")
                    checker.pretty_print(rules)
                    print("\nPlease try again.")

            # Once a valid password is entered, show the strength label
            label = checker.strength_label(score)
            print(f"\nStrength score: {score}/5")
            print(f"Password strength: {label}")
