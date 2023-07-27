from datetime import datetime as dt
from time import sleep

from app.tg_message import send_message
from settings import DT_FORMAT, RETRY_TIME


def main():
    while True:
        send_message()
        date_time = dt.now().strftime(DT_FORMAT)
        print(date_time)
        sleep(RETRY_TIME)


if __name__ == "__main__":
    main()
