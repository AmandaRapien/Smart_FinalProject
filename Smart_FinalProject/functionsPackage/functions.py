'''
Name: Kevin Wilson, Bill Tummler, Amanda Rapien, Grace Hertzfeld
email: wilso3kv@mail.uc.edu, tummlewm@mail.uc.edu, rapienaa@mail.uc.edu, hertzfgc@mail.uc.edu
Assignment: Smart - Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can 
decrypt a file and display a photo.
Citations:
Anything else that's relevant:
'''
import os, json


f = open('english.txt','r')
test = open('EncryptedGroupHints.json')
file = f.readlines()

print(file)

#file.replace('\n','')



parsed_json = json.load(test)

print(parsed_json)
json = (parsed_json['Smart'])
for num in json:
    print(file[int(num)])

'''
text = []
for item in file:
        print(json[int(item)])
print(text)
'''