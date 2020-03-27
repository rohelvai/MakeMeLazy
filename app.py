#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: app.py
# Created: Sunday, 15th March 2020 2:12:21 am
# Author: Mohammad Rohel Ahmed (mail2rohel@gmail.com)
# -----
# Last Modified: Sunday, 15th March 2020 2:12:31 am
# Modified By: Mohammad Rohel Ahmed (mail2rohel@gmail.com)
# -----
# Copyright (c) 2020 xRisk
###
import os
import sys
import json
import requests as rq
from time import sleep

api_key = "a38b94c4454cff593f431344a4320fbc0d6089b823665f80d3d80e556e85dd57"


def req(data):
    url = "https://www.virustotal.com/vtapi/v2/url/scan"
    res = rq.post(url, data=data)
    # print(res.text)
    resp = res.json()
    return resp["permalink"], resp["scan_id"]


def report(id):
    url = "https://www.virustotal.com/vtapi/v2/url/report"
    params = {
        "apikey": api_key,
        "resource": id
    }

    res = rq.get(url, params=params)
    with open(f"{id}.json", "w") as f:
        f.write(json.dumps(res.json(), indent=4))

    print(f"[+] Data written Successfully to: {id}.json")


if __name__ == "__main__":
    # print(analyse(req(data)))
    if len(sys.argv) < 2:
        print("[-] Please pass a URL as argument...")
        sys.exit()

    data = {
        "apikey": api_key,
        "url": sys.argv[1]
    }

    link, id = req(data)
    print(f"[+] Got ID: {id}\n[+] Scan is in queue. Please wait...")
    sleep(3)
    report(id)
    # print(link, id)
