import requests
import json

url='http://172.16.1.82/ins'
switchuser='cisco'
switchpassword='cisco'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show version",
      "version": 1.2
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()

sys_ver = response['result']['body']['sys_ver_str']
print ("The Software Version is: " + sys_ver)
header_str = response['result']['body']['header_str']
print(header_str)
host_name = response['result']['body']['host_name']
print("The hostname is: "  + host_name) 
