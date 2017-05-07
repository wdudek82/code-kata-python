import threading
import time
import random


class BankAccount(threading.Thread):

    balance = 100
    thread_lock = threading.Lock()

    def __init__(self, name, money_request):
        threading.Thread.__init__(self)

        self.name = name
        self.money_request = money_request

    def run(self):
        self.thread_lock.acquire()

        BankAccount.get_money(self)

        self.thread_lock.release()

    @staticmethod
    def get_money(customer):
        print("{} tries to withdraw ${} at {}".format(
            customer.name, customer.money_request, time.strftime("%H:%M:%S", time.gmtime())
        ))

        if BankAccount.balance - customer.money_request >= 0:
            BankAccount.balance -= customer.money_request
            print("New account balance: ${}\n".format(BankAccount.balance))
        else:
            print("Not enough money in account")
            print("Current balance: ${}\n".format(BankAccount.balance))

        time.sleep(3)

doug = BankAccount("Doug", 1)
paul = BankAccount("Paul", 100)
sally = BankAccount("Sally", 50)

threads = (doug, paul, sally)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("Execution Ends")