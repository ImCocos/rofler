import os
from time import sleep
import requests
from main import update_cmd, update_interval_sec
from bs4 import BeautifulSoup as bs

githubURL = 'https://github.com/ImCocos/rofler/releases'

def update():
    os.system(update_cmd)
    print('Update........')

def check_update() -> bool:
    with open('last_update.txt') as f:
        last_commit = f.read()

    update_commit = get_new_commit()

    if last_commit != update_commit:
        update()

    with open('last_update.txt', 'w') as f:
        f.write(update_commit)
def get_new_commit() -> str:
    page = requests.get(githubURL)
    soup = bs(page.text, 'html.parser')
    return soup.find('code', class_='f5 ml-1 wb-break-all').text

while True:
    print('Update Checker active')
    sleep(update_interval_sec)
    if check_update():
        update()