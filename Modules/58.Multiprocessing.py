# Multiprocessing
# -----
# Running tasks in parallel on different cpu cores, bypasses GIL used for threading
#               multiprocessing = better for cpu bound tasks (heavy cpu usage)
#               *multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    # we can run as many as the pc cpu count is, mine is 8 so we can run 8 processes at the same time
    print(cpu_count())

    # to speed up the process we can divide it to same values into 4 places
    # or as many cpu counts our pc has
    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))
    a.start()
    b.start()
    c.start()
    d.start()

    a.join()
    b.join()
    c.join()
    d.join()
    print("Finished in: ", time.perf_counter(), "seconds")


if __name__ == "__main__":
    main()


