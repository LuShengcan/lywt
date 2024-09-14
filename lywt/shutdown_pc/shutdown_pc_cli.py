import os
from datetime import datetime

def shutdown(time:int):
    os.system("shutdown /a")
    os.system(f'shutdown /s /t {time}')


def shutdown_after(hours:int, minutes:int):
    time = hours * 60 * 60 + minutes * 60
    shutdown(time)


def shut_down_at(hour:int, minute:int):
    now = datetime.now()
    target_time = now.replace(hour=hour, minute=minute)
    time = int((target_time - now).total_seconds())
    if time >= 0:
        shutdown(time)
