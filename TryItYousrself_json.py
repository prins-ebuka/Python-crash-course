#Exercise 10-11
import json

user_number = input('Input any number:')

fav_no = 'user_number.json'
with open(fav_no, 'w') as f:
    json.dump(user_number, f)
    print(f"Your favourite number is {user_number}!")

fav_no = 'user_number.json'
with open(fav_no) as f:
    user_number = json.load(f)
    print(f"We didn't forget your favourite number {user_number}!")