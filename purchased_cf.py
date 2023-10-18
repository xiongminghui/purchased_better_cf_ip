import requests
import json
import os
api_key = os.environ.get("API_KEY")

def get_ip_region(ip):
    res = requests.get(f"http://ip-api.com/json/{ip}?lang=zh-CN")
    data = res.json()
    region = "美国"
    if data["country"] != "":
        region = data["country"]
    return str(region)

# get_ip_region("192.169.113.194")
# exit(0)
def add_region_to_ips(data):
    info = data["info"]
    for key in info:
        for item in info[key]:
            ip = item["ip"]
            region = get_ip_region(ip)
            item["region"] = str(region)
    return data


headers = {'Content-Type': 'application/json'}
dataJson = {"key": api_key, "type": "v4"}
response = requests.post('https://api.hostmonit.com/get_optimization_ip', json=dataJson, headers=headers)
if response.status_code != 200:
    print("获取失败！")
    exit(0)
data = response.json()
if data["code"] != 200:
    exit()
result = add_region_to_ips(data)

output = json.dumps(result, indent=4)
# print(output)
with open("better_ip.json", "w") as file:
    file.write(output)


