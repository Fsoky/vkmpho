import argparse
import asyncio
import os

from vkbottle import API, VKAPIError

parser = argparse.ArgumentParser()
parser.add_argument("-u", type=str)
parser.add_argument("--count", type=int, default=0)
options = parser.parse_args()

api = API("TOKEN")


async def get_user_id(user_id=None):
    if user_id is None:
        user_id = options.u

    if not user_id.isdigit():
        if not os.path.exists(user_id):
            user_id = await api.utils.resolve_screen_name(screen_name=user_id)
            user_id = user_id.object_id
        else:
            with open(user_id, "r", encoding="utf-8") as file:
                user_id = file.readlines()

    return user_id


async def get_photos_from_user():
    user_id = await get_user_id()

    try:
        if not isinstance(user_id, list):
            photos = [await api.photos.get_all(owner_id=user_id)]
        else:
            photos = []
            for uid in user_id:
                clear_uid = await get_user_id(uid.replace("\n", ""))
                photos.append(await api.photos.get_all(owner_id=clear_uid))

        return photos
    except VKAPIError[19]:
        print("Content is blocked")
    except VKAPIError[30]:
        print("Profile is private")


async def handler():
    photos = await get_photos_from_user()
    counter = 0

    for photo_item in photos:
        for photo in photo_item.items:
            if options.count > 0:
                if counter == options.count:
                    break

            if (photo.lat and photo.long) is not None:
                print(f"ID: https://vk.com/id{photo.owner_id}\nLatitude: {photo.lat}\nLongitude: {photo.long}\nURL: {photo.sizes[9].url}\n")

            counter += 1


asyncio.run(handler())
