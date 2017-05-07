import threading
import time
import random


def showtime(num, action):
    print("Thread {} {} at {}".format(
        num, action, time.strftime("%H:%M:%S", time.gmtime())
    ))



def execute_thread(ident):
    showtime(ident, "sleeps")

    rand_sleep = random.randint(1, 5)
    time.sleep(rand_sleep)

    showtime(ident, "stops")


for i in range(10):
    thread = threading.Thread(target=execute_thread, args=(i,))
    thread.start()

    print("Active threads: ", threading.active_count())
    print("Thread objects: ", threading.enumerate())
