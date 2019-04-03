#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request
import requests
import random

app = Flask(__name__)


@app.route("/callme", methods=['POST'])
def callme():
    data = request.get_json(force=True)
    host = data.get("myhost", None)
    port = data.get("myport", None)
    if not host and not port:
        key_id = random.randint(0, 1000)
        resp = requests.get("http://{}:{}/{}".format(host, port, key_id))
        if resp.status_code() == 200:
            print(resp.content, key_id)
        return "Nice"
    return "Error"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8070")
