# vkmpho
Metadata from VK photos (beta)

### Tools
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![VkBottle](https://img.shields.io/badge/VkBottle-4.0-pink?style=for-the-badge&logo=vk)
![Asyncio](https://img.shields.io/badge/Asyncio-red?style=for-the-badge)

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
- Run the script
```
$ python3 vkmpho.py -u USER_NAME_OR_ID --count 12
```

If photo has some geo data, script returns info about it:
```bash
Latitude: 123.0000
Longitude: 456.0000
URL: https://vk.com/userapi.....
```
