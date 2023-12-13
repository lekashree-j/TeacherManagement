import json
import os
# File to store movie records
data_json = 'static/data.json'

#
def get_all():
    if not os.path.exists('static/data.json'):
        with open(data_json, 'w') as file:
            json.dump([], file)

    with open(data_json, 'r') as file:
        #try:
            teachers = json.load(file)
        #except json.JSONDecoder:
            #data = []
    return teachers

def add_teacher(details):
    teachers = get_all()
    teachers.append(details)
    write_teacher(teachers)

def delete_teachers(name):
    teachers = get_all()
    teachers = [teacher for teacher in teachers if teacher['name'] != name]
    write_teacher(teachers)

def write_teacher(teachers):
    with open(data_json, 'w') as file:
        json.dump(teachers, file, indent=2)