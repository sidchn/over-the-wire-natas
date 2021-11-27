#!/usr/bin/python3

import requests
import re
import os

username="natas4"
password=os.getenv("natas_pass")

url = "http://{0}.natas.labs.overthewire.org/".format(username)

headers={'referer':'http://natas5.natas.labs.overthewire.org/'}
response = requests.get(url,auth=(username,password),headers=headers)



flag = re.findall('natas5 is (.*)',response.text)[0]

print(flag)