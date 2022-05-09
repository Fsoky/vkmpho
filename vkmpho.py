import argparse
import asyncio

from vkbottle import API, VKAPIError

parser = argparse.ArgumentParser()
parser.add_argument("-u", type=str)
parser.add_argument("--count", type=int, default=0)
options = parser.parse_args()

api = API("TOKEN")


async def handler():
    user_id = options.u
    if not user_id.isdigit():
        user_id = await api.utils.resolve_screen_name(screen_name=user_id)
        user_id = user_id.object_id

    try:
        photos = await api.photos.get_all(owner_id=user_id)

        counter = 0
        for photo in photos.items:
            if options.count > 0:
                if counter == options.count:
                    break

                if (photo.lat and photo.long) is not None:
                    print(f"Latitude: {photo.lat}\nLongitude: {photo.long}\nURL: {photo.sizes[9].url}\n")
            counter += 1
    except VKAPIError[19]:
        print("Content is blocked")
    except VKAPIError[30]:
        print("Profile is private")


asyncio.run(handler())
