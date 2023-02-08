import json
import os

dict = {
    "first_name" : "Sammy",
    "last_name" : "Shark",
    "location" : "Ocean",

    "websites" : [
        {
        "description" : "work",
        "URL" : "https://www.digitalocean.com/"
        },
        {
        "desciption" : "tutorials",
        "URL" : "https://www.digitalocean.com/community/tutorials"
        }
        ],
        "social_media" : [
        {
        "description" : "twitter",
        "link" : "https://twitter.com/digitalocean"
        },
        {
        "description" : "facebook",
        "link" : "https://www.facebook.com/DigitalOceanCloudHosting"
        },
        {
        "description" : "github",
        "link" : "https://github.com/digitalocean"
        }
    ]
}

def read_json():
    data = []
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data;

def write_json(data):
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

if not os.path.isfile("data.json"):
    write_json(dict)
    print("Данные записаны в файл data.json")
else:
    print("Чтение данных из файла data.json")
    data_json = read_json()
    print(data_json)