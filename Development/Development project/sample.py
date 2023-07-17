import csv


data = [
    {'username': 'john123', 'regno': '123456', 'gmail': 'john123@gmail.com', 'dept': 'Computer Science', 'year': '2022'},
    {'username': 'mary456', 'regno': '987654', 'gmail': 'mary456@gmail.com', 'dept': 'Electrical Engineering', 'year': '2023'}
]
fieldnames= ["username", "regno", "gmail", "dept", "year"]
with open("Agent.csv", 'w', newline="") as file:
    writer = csv.DictWriter(file, fieldnames )




