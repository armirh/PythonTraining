# daemon threads = a thread that runs in the background, not important for program to run
#                   your program will not wait for the daemon threads to complete before exiting
#                   non-daemon threads can't normally be killed, stay alive until task is complete
#

#                   examples: background tasks, waiting for input, long running process

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, " seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

answer = input("Do you wish to exit? ")
