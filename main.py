from password import Password
from checker import PasswordChecker

def main():
    # Create a PasswordChecker instance that will handle all validation,
    # scoring, history saving, and password generation.
    checker = PasswordChecker()

    while True:
        # Display the main menu options to the user.
        print("\nPassword Checker Menu")
        print("1. Check a password")
        print("2. View password history")
        print("3. Generate a random strong password")
        print("4. Quit")

        # Get the user's menu choice as a string.
        choice = input("Choose an option (1-4): ")

     
        # Option 1 — password check
        
        if choice == "1":
            # Explain the password rules to the user.
            print("\nYour password must meet ALL of these rules:")
            print("At least 8 characters long")
            print("At least one uppercase letter")
            print("At least one lowercase letter")
            print("At least one digit")
            print("At least one symbol")

            while True:
                # Ask the user to enter a password.
                pwd_input = input("\nEnter a password: ")

                # Wrap the raw string inside a Password object.
                pwd = Password(pwd_input)

                # Run the password through the checker to evaluate each rule.
                rules = checker.check(pwd)

                # Convert the rule results into a numeric score (0–5).
                score = checker.score(rules)

                # If all rules passed, accept the password.
                if score == 5:
                    print("\nPassword accepted!")
                    checker.pretty_print(rules)  # Show rule-by-rule results.
                    break
                else:
                    # If not all rules passed, show the failed rules
                    # and ask the user to try again.
                    print("\nPassword does NOT meet the requirements:")
                    checker.pretty_print(rules)
                    print("\nPlease try again.")

            # Convert the numeric score into a human-readable label.
            label = checker.strength_label(score)
            print(f"\nStrength score: {score}/5")
            print(f"Password strength: {label}")

            # Save the accepted password to history.txt.
            checker.save_to_history(pwd)
            print("Password saved to history.txt")

        # Option 2 — viewing password history
       
        elif choice == "2":
            # Display all previously saved passwords.
            checker.view_history()

       
        # Option 3 — generating random passwords
       
        elif choice == "3":
            print("\nGenerating a strong random password...")

            # Create a new random password that meets all rules.
            generated = checker.generate_random_password()

            print(f"\nYour generated password: {generated}")

            # Save the generated password to history.
            pwd = Password(generated)
            checker.save_to_history(pwd)
            print("Password saved to history.txt")

       
        # Option 4 — quit the program
  
        elif choice == "4":
            print("Goodbye!")
            break
       
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
