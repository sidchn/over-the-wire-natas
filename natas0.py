#!/usr/bin/python3

import requests
import re
import os

username='natas0'
password='natas0'

url="http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url,'GET',auth=(username,password))

flag = re.findall("<!--The password for natas1 is (.*) -->",response.text)[0]
print(flag)
