import os
from datetime import datetime

def greet():
    msg = os.getenv("APP_MESSAGE", "Default Message")

    # write to log file
    with open("app.log", "a") as f:
        f.write(f"{datetime.now()}  {msg}\n")

    return msg

if __name__ == "__main__":
    print(greet())

