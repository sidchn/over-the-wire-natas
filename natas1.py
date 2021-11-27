#!/usr/bin/python3

import requests
import re
import os

username='natas1'
#set the password you get for natas1 as an environment variable.
password=os.getenv("natas_pass") 


url="http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url,'GET',auth=(username,password))

flag = re.findall("<!--The password for natas2 is (.*) -->",response.text)[0]
print(flag)