import requests
myip = requests.get("https://api.ipify.org/?format=json").json()['ip']
print('IPv4 Address: ' + myip)