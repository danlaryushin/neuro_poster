from datetime import datetime as dt
from time import sleep

from tg_message import send_message

RETRY_TIME = 300


def main():
    while True:
        send_message()
        date_time = dt.now().strftime("%I:%M%p on %B %d, %Y")
        print(date_time)
        sleep(RETRY_TIME)


if __name__ == "__main__":
    main()
