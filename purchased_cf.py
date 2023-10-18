import math

import requests
import json
import os
api_key = os.environ.get("API_KEY")
ip_token = os.environ.get("IP_TOKEN")
def get_ip_region(ip):
    r = requests.get(f"https://ipinfo.io/{ip}?token={ip_token}")
    ipData = r.json()
    if r.status_code != 200:
        exit(0)
    if "country" not in ipData:
        exit(0)
    return str(ipData["country"])

def add_region_to_ips(data):
    info = data["info"]
    for key in info:
        for item in info[key]:
            ip = item["ip"]
            region = get_ip_region(ip)
            item["region"] = region
    return data


# headers = {'Content-Type': 'application/json'}
# dataJson = {"key": api_key, "type": "v4"}
# response = requests.post('https://api.hostmonit.com/get_optimization_ip', json=dataJson, headers=headers)
# if response.status_code != 200:
#     print("获取失败！")
#     exit(0)
response = requests.get('https://raw.githubusercontent.com/xiongminghui/cloudflare-better-ip/main/html/purchased_cf_ip.json')
data = response.json()
if data["code"] != 200:
    exit()
result = add_region_to_ips(data)

output = json.dumps(result, ensure_ascii=False)
print(output)
# with open("better_ip.json", "w") as file:
#     file.write(output)
