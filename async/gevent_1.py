from gevent import sleep


def hello():
    print('Hello')
    sleep(3)
    print('World!')


if __name__ == '__main__':
    hello()
