import requests


def check_success(url):
    if requests.get(url):
        return "Success"
    return "Fail"
