import os
import sys

import requests


def save_pics(dir_path: str):
    images_list = list()

    url = "http://shibe.online/api/shibes?count=100&urls=true&httpsUrls=true"
    api_answer = requests.get(url).json()
    for image_url in api_answer:
        content_length = int(requests.head(image_url).headers["Content-Length"])
        images_list.append(
            {
                "url": image_url,
                "content_length": content_length
            }
        )

    sorted_images_list = sorted(images_list, key=lambda x: x["content_length"], reverse=True)
    print(sorted_images_list)
    large_five_pics = [sorted_images_list[i] for i in range(5)]
    print(large_five_pics)

    for item in large_five_pics:
        image_url = item["url"]
        r = requests.get(image_url)
        with open("{}/{}".format(dir_path, image_url.split("/")[-1]), "wb") as f:
            f.write(r.content)

    return True


if __name__ == '__main__':
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = os.getcwd()

    save_pics(dir_path=arg)
