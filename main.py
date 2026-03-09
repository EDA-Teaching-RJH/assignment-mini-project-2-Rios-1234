
def main():
    # Create a PasswordChecker instance to handle all password logic
    checker = PasswordChecker()

    # command line mode (sys.argv)
   
    # If the user provided command-line arguments, handle them here
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()  # First argument = command

        # Show password history
        if cmd == "history":
            cowsay.stegosaurus("Showing password history!")
            checker.view_history()
            return

        # Generate a random password
        elif cmd == "generate":
            cowsay.dragon("Generating a mighty password!")
            pwd = checker.generate_random_password()
            print(f"Generated password: {pwd}")

            # Save generated password as strong by default
            checker.save_to_history(Password(pwd), 5, "Strong")
            return

        # Check a password directly from the command line
        elif cmd == "check":
            # Must include a password argument
            if len(sys.argv) < 3:
                print("Usage: python main.py check <password>")
                return

            raw = sys.argv[2]
            pwd = Password(raw)
             # Run password through all rules
            rules = checker.check(pwd)
            score = checker.score(rules)
            label = checker.strength_label(score)

            cowsay.cow("Password check results!")
            checker.pretty_print(rules)

            print(f"\nScore: {score}/5")
            print(f"Strength: {label}")
            return
             # Show only the strength label (no rule breakdown)
        elif cmd == "strength":
            if len(sys.argv) < 3:
                print("Usage: python main.py strength <password>")
                return

            raw = sys.argv[2]
            pwd = Password(raw)

            rules = checker.check(pwd)
            score = checker.score(rules)
            label = checker.strength_label(score)

            cowsay.tux(f"Strength: {label}")
            return
             # Show statistics about past passwords
        elif cmd == "stats":
            cowsay.turkey("Password statistics!")
            checker.show_stats()
            return
            # Clear password history (CLI version)
        elif cmd == "clear-history":
            confirm = input("Are you sure you want to clear history? (y/n): ").lower()
            if confirm == "y":
                cowsay.ghostbusters("Clearing history!")
                checker.clear_history()
                print("History cleared.")
            else:
                print("Cancelled.")
            return
            
            #Demo mode starts here
             elif cmd == "demo":
            cowsay.beavis("Welcome to demo mode!")

            # Demo: checking a password
            print("\n--- DEMO: Checking a password ---")
            pwd = Password("Aa1!demo")
            rules = checker.check(pwd)
            checker.pretty_print(rules)
            score = checker.score(rules)
            label = checker.strength_label(score)
            print(f"Score: {score}/5 | Strength: {label}")
        # Demo: generating a password
            print("\n--- DEMO: Generating a password ---")
            generated = checker.generate_random_password()
            print(f"Generated: {generated}")

            # Demo: saving to history
            print("\n--- DEMO: Saving to history ---")
            checker.save_to_history(Password(generated), 5, "Strong")
            print("Saved to history.csv")

            # Demo: showing stats
            print("\n--- DEMO: Showing stats ---")
            checker.show_stats()

            cowsay.tux("Demo complete!")
            return
         # Unknown command entered
        else:
            cowsay.ghostbusters("Unknown command!")
            print("Valid commands: history, generate, check, strength, demo,clear history,stats")
            return
            while True:
        # Display menu options
        print("\nPassword Checker Menu")
        print("1. Check a password")
        print("2. View password history")
        print("3. Generate a random strong password")
        print("4. Clear password history")
        print("5. Quit")

        choice = input("Choose an option (1-5): ")

        # Option 1: Check password
        
        if choice == "1":
            print("\nYour password must meet ALL of these rules:")
            print("At least 8 characters long")
            print("At least one uppercase letter")
            print("At least one lowercase letter")
            print("At least one digit")
            print("At least one symbol")
             # Loop until user enters a valid password
            while True:
                pwd_input = input("\nEnter a password: ")
                pwd = Password(pwd_input)

                rules = checker.check(pwd)
                score = checker.score(rules)

                if score == 5:
                    cowsay.cow("Moo! Strong password!")
                    print("\nPassword accepted!")
                    checker.pretty_print(rules)
                    break
                else:
                    cowsay.tux("Try again,!")
                    print("\nPassword does NOT meet the requirements:")
                    checker.pretty_print(rules)
                     # Show final strength label
            label = checker.strength_label(score)
            print(f"\nStrength score: {score}/5")
            print(f"Password strength: {label}")

            # Save password to history
            checker.save_to_history(pwd, score, label)
            print("Password saved to history.csv")
             # Option 2: View history
       
        elif choice == "2":
            cowsay.stegosaurus("Here are your past passwords!")
            checker.view_history()

      
        # Option 3: Generate password
        
        elif choice == "3":
            cowsay.dragon("Forging a mighty password...")
            generated = checker.generate_random_password()

            print(f"\nYour generated password: {generated}")

            pwd = Password(generated)
            checker.save_to_history(pwd, 5, "Strong")
            print("Password saved to history.csv")


