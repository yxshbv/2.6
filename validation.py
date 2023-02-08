import json
import os
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "first_name" : {"type" : "string"},
        "last_name" : {"type" : "string"},
        "location" : {"type" : "string"}
    },
    "required": ["first_name", "last_name", "location"],
}


def read_json():
    data = []
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data;
    
print("Чтение данных из файла data.json")
data_json = read_json()

val = validate(data_json, schema)

if val == None:
    print("Данные успешно прошли валидацию!")

print(data_json["first_name"])