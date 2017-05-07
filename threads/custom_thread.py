import threading
import time
import random


class CustomThread(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)

        self.name = name

    def run(self):
        self.get_time(self.name)
        self.get_time(self.name, "execution ends")

    @staticmethod
    def get_time(name, action="sleeps"):
        print("Thread {} {} at {}".format(
            name, action, time.strftime("%H:%M:%S", time.gmtime())
        ))

        rand_sleep = random.randint(1, 5)

        time.sleep(rand_sleep)

thread1 = CustomThread("First")
thread2 = CustomThread("Second")

threads = (thread1, thread2)
for thread in threads:
    thread.start()

    print("Thread {name} is alive: {alive}".format(
        name=thread.getName(),
        alive=thread.is_alive())
    )
for thread in threads:
    thread.join()

print("Execution Ends")