'''
Created on Nov 22, 2022

@author: KevinWilson
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