import calc
import current_time
import notes
import perfect_guess
import web_browser

### Total 250 lines of code

def main():
    while True:
        print("\n====== My Phone ======")
        print("\n=== Main Menu ===")
        print("1. Calculator")
        print("2. Perfect Guess Game")
        print("3. Current Time Display")
        print("4. Notes")
        print("5. Web Browser")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            calc.run_calculator()
        elif choice == '2':
            perfect_guess.play_game()
        elif choice == '3':
            current_time.show_time()
        elif choice == '4':
            notes.manage_notes()
        elif choice == '5':
            web_browser.open_browser()
        elif choice == '6':
            print("Goodbye!")
            break 
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()