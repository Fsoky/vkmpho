import argparse
import asyncio
import io
import time

import aiohttp
import aiofiles

from PIL import Image as PILImage
from exif import Image

from vkbottle import API, VKAPIError

parser = argparse.ArgumentParser()
parser.add_argument("-u")
parser.add_argument("--count", type=str, default=10)
options = parser.parse_args()

api = API("token")


async def handler():
    start_count = 0

    try:
        user_id = options.u
        if not options.u.isdigit():
            user_id = await api.utils.resolve_screen_name(screen_name=options.u)
            user_id = user_id.object_id

        photos = await api.photos.get_all(owner_id=user_id)
        print(f"Count: {photos.count}")

        for photo in photos.items:
            if start_count == options.count:
                break

            async with aiohttp.ClientSession() as session:
                async with session.get(photo.sizes[0].url) as response:
                    photo_bytes = await aiohttp.StreamReader.read(response.content)
                    filename = time.time()

                    img = PILImage.open(io.BytesIO(photo_bytes))
                    img.save(f"./spho/{filename}.jpg")

                    async with aiofiles.open(f"./spho/{filename}.jpg", mode="rb") as file:
                        content_of_photo = Image(await file.read())

                        if content_of_photo.has_exif:
                            print(f"[+] {filename}.jpg has exif")

                    start_count += 1
    except VKAPIError[19]:
        print("Access error.")


asyncio.run(handler())
