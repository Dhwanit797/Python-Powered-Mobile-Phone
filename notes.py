import os

def manage_notes():
    print("Notes app is running!")

    print("\n### Notepad ###")
    choice = int(input("Enter \n1. For new note \n2. For re-writing existing one \n3. For reading a note: "))

    if choice == 1:
        name = input("Enter the name of the file: ")
        name += ".txt"
        txt = input("Enter what you want to write:\n")
        try:
            with open(name, "w") as f:
                f.write(txt)
            print(f"File '{name}' created successfully!")

            choice2 = int(input("Enter 1. To read the file \n2. To exit the program: "))
            if choice2 == 1:
                with open(name, "r") as f:
                    read = f.read()
                    print(read)
            elif choice2 == 2:
                print("Exited the program")
            else:
                print("Please enter a valid number")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif choice == 2:
        name = input("Enter the name of the note you need to edit: ")
        name += ".txt"
        if os.path.exists(name):
            txt = input("Enter what you want to write: \n")
            try:
                with open(name, "w") as f:
                    f.write(txt)
                print(f"File '{name}' updated successfully!")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print(f"File '{name}' not found!")

    elif choice == 3:
        name = input("Enter the name of the file you want to read: ")
        name += ".txt"
        try:
            with open(name, "r") as f:
                read = f.read()
                print(read)
        except FileNotFoundError:
            print(f"File '{name}' not found!")
        except Exception as e:
            print(f"An error occurred: {e}")

    else:
        print("Please enter a valid number")

if __name__ == "__main__":
    manage_notes()