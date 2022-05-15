# vkmpho
Metadata from VK photos (beta)

### Tools
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![VkBottle](https://img.shields.io/badge/VkBottle-4.0-pink?style=for-the-badge&logo=vk)
![Asyncio](https://img.shields.io/badge/Asyncio-red?style=for-the-badge)

### Options
|Option|Description|
|------|-----------|
|-u    |User name or ID for get all photos from wall|

## Getting started

- Download repository from GitHub
```
$ git clone https://github.com/Fsoky/vkmpho.git
```
- Change directory and setup dependencies
```
$ cd vkmpho/
$ pip3 install vkbottle
```
- Get access token for your account ([you can do it here](https://vkhost.github.io/))
- Open file in editor and replace word *TOKEN* to your access token
```py
api = API("TOKEN")
```

- Run the script
```
$ python3 vkmpho.py -u USER_NAME_OR_ID --count 12
```
*Also you can pass the TXT file with IDs*
```
$ python3 vkmpho.py -u some_user_ids.txt
```

If photo has some geo data, script returns info about it:
```bash
ID: https://vk.com/id000000
Latitude: 123.0000
Longitude: 456.0000
URL: https://vk.com/userapi.....
```
