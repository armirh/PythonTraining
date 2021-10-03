# thread = a flow of execution. Like a separate order of functions.
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock), only one thread at a time
#           allows only one thread to hold the control of the python interpreter

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time

print(threading.active_count())  # counts the number of threads
print(threading.enumerate())


# Example

def eat_breakfast():
    time.sleep(3)
    print("You just ate breakfast!")


def drink_coffee():
    time.sleep(4)
    print("You just drank coffee!")


def get_ready():
    time.sleep(5)
    print("You just studied!")


# where as here, we assign each function in separate threads, and the run-time will be faster, around 5 secs
x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=get_ready(), args=())
z.start()

# we can make our MainThread wait until the other threads are done
# x.join()
# y.join()
# z.join()

# all these tasks take around 12secs to run, because the MainThread is running them at the same time in order
# eat_breakfast()
# drink_coffee()
# get_ready()

# how long it takes our thread to finish
print(time.perf_counter())
