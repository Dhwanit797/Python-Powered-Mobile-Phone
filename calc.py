def run_calculator():
    print("Calculator is running!")
    while True:
        try:
            expression = input("Enter expression (Enter ""0^0"" to exit the calc) :  ")
            if expression == "0^0":
                print("Exiting calculator...")
                break
            ans = int(eval(expression))
            print(ans)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_calculator()