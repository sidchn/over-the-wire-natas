#!/usr/bin/python3

import requests
import re
import os


username="natas8"
password=os.getenv("natas_pass")
auth=(username,password)

url = "http://{0}.natas.labs.overthewire.org/".format(username)

response = requests.get(url+'index-source.html',auth=auth)
#print(response.text)
# #1. php loose comparison
# #2. reversible operations
data={"secret":"oubWYf2kBq",'submit':'Submit Query'}
response2 = requests.post(url,auth=auth,data=data)
flag = re.findall("natas9 is (.*)",response2.text)[0]

print(flag)