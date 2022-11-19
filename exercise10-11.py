import json

fav_no = 'user_number.json'
with open(fav_no) as f:
    user_number = json.load(f)
    print(f"We didn't forget your favourite number {user_number}!")