import threading
import time


def a() -> None:
    while True:
        time.sleep(2)
        print('a', end='')

def b() -> None:
    while True:
        input('Message: ')

def main() -> None:
    threading.Thread(target=a).start()
    threading.Thread(target=b).start()


if __name__ == '__main__':
    main()
