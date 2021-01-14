import json
import csv


with open("users.json", "r") as users:
    parsed_users = json.load(users)
    user_list = []
    for user in parsed_users:
        user_list.append(dict(name=user["name"],gender=user["gender"],address=user["address"]))

with open('books.csv') as File:
    reader = csv.DictReader(File)
    book_list = []
    for row in reader:
        book_list.append(dict(title=row["Title"],author=row["Author"],height=row["Height"]))

i=0
for user in user_list:
    user.update({"books": book_list[i]})
    i = i+1

with open("example.json", "w") as example:
    example.write(json.dumps(user_list))


