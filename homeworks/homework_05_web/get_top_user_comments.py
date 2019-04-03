import sys
import asyncio
import requests
from bs4 import BeautifulSoup
import csv
import collections


async def response(url):
    resp = requests.get(url)
    if resp.ok:
        soup = BeautifulSoup(resp.text, "html.parser")
        div = soup.findAll("div", attrs={"class": ["comment__head"]})
        if len(div) < 100:
            return 0
        else:
            return div
    else:
        print("Invalid link")


async def parse(url):
    username = []
    result = []
    top = []
    div = await response(url)
    for i in range(len(div)):
        username.append((div[i].find("a")["data-user-login"]))
    common = collections.Counter(username).most_common()
    common.sort(key=lambda x: (-x[1], x[0]))
    for i in range(len(common)):
        result.append(url)
        result.append(common[i][0])
        result.append(common[i][1])
        top.append(result)
        result = []
    with open("top_user_comments.csv", "a", newline="") as f:
        lines = csv.writer(f)
        lines.writerows(top)


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]
    open(filename, "w").close()
    tasks = []
    ioloop = asyncio.get_event_loop()
    for i in links:
        tasks.append(ioloop.create_task(parse(i)))
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
