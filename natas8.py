#!/usr/bin/python3

import requests
import re
import os
import html2text
import base64

username="natas8"
password=os.getenv("natas_pass")


auth=(username,password)

url = "http://{0}.natas.labs.overthewire.org/".format(username)


h = html2text.HTML2Text()


response = requests.get(url+'index-source.html',auth=auth)
rendered_response = h.handle(response.text)
encodedsecret=re.findall('"(.*)";',rendered_response)[0]

bytes_object = bytes.fromhex(encodedsecret)[::-1]
secret = base64.b64decode(bytes_object)



data={"secret":secret,'submit':'Submit Query'}
response2 = requests.post(url,auth=auth,data=data)
flag = re.findall("natas9 is (.*)",response2.text)[0]

print(flag)