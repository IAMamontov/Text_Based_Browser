import sys
import os
import requests
from collections import deque
from bs4 import BeautifulSoup
from colorama import Fore, Style

history = deque()

if len(sys.argv) == 2:
    try:
        os.mkdir(sys.argv[1])
    except FileExistsError:
        print("Directory ", sys.argv[1], " already exists")
    finally:
        save_path = os.path.join(os.path.curdir, sys.argv[1])
else:
    save_path = os.path.curdir
users_url = input()
while not users_url == "exit":
    if len(users_url.split(".")) > 1:
        if not users_url.startswith("http://"):
            users_url = "http://" + users_url
        history.append(users_url)
        if requests.get(users_url):
            respond = requests.get(users_url)
            name = users_url.split(".")[len(users_url.split(".")) - 2]
            if name.startswith("http://"):
                name = name.replace("http://", "", 1)
            save_name = os.path.join(save_path, name)
            with open(save_name, "w") as f:
                soup = BeautifulSoup(respond.content, "html.parser")
                for tag in soup.find_all(["title", "p", "h1", "h2", "h3", "h4", "h5", "h6", "a", "ul", "ol", "li"]):
                    if tag.string is not None:
                        if tag.name == "a":
                            print(Fore.BLUE + tag.string + Style.RESET_ALL)
                        else:
                            print(tag.string)
                        f.write(tag.string + "\n")
        else:
            history.pop()
            print("URL error: no such page")
    elif len(users_url.split(".")) == 1:
        save_name = os.path.join(save_path, users_url)
        if users_url == "back":
            if len(history) > 1:
                history.pop()
                users_url = history.pop()
                continue
            else:
                continue
        elif os.path.exists(save_name):
            with open(save_name, "r") as f:
                read = f.read()
                print(read)
        else:
            print("URL error: no dot or no such saved page")

    users_url = input()
