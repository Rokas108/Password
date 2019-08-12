"""A program that allows the user to create accounts with passwords, log in to the accounts and check passwords that they have forgotten"""
import json 

import functions as f

input_text = '\nIf you wish to quit press "Q", to log in press "L", to sign up press "S":'
command = "start"
filename = 'dict.json'


with open(filename) as d:
    password_dict = json.load(d)   
print(password_dict)

while  command == "Q" or command == "L" or command == "S" or command == "D" or command == 'start':
    command = input(input_text)
    if command.isalpha():
        command = command.upper()
        if command == "Q":
            print(command)
            break
        if command == "L":
            f.login(password_dict)
        if command == "S":
            f.sign_up(password_dict)
        if command == "D":
            print(password_dict)
        else:
            command = "start"
    else:
        command = "start"

with open(filename, 'w') as d:
    json.dump(password_dict, d)



