#!/usr/bin/python
f=open("/root/Python/json.txt","r")
s=f.read()
import json
log=json.loads(s)
print log['Records'][0]['responseElements']['user']['userName']

