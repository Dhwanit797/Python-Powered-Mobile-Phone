import random

def play_game():
    print("Perfect Guess Game is running!")
    
    while True:
        comp_choice = random.randint(1, 20)
        attempt = 0

        while True:
            try:
                my_choice = int(input("Enter a number between 1 and 20: "))
                attempt += 1

                if my_choice == comp_choice:
                    print("You Win!")
                    print(f"Total attempts = {attempt}")
                    break

                elif my_choice < comp_choice:
                    print("Too low")

                elif my_choice > comp_choice:
                    print("Too high")

            except ValueError:
                print("Please enter a valid number!")

        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    play_game()