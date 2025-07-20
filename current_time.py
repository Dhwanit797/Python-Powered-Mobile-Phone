import time

def show_time():
    print("Current time display is running!")

    start_time = time.time()

    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("Current time:", current_time)
        time.sleep(1)

        if time.time() - start_time >= 5:
            print("Exiting current time display after 5 seconds.")
            break

if __name__ == "__main__":
    show_time()