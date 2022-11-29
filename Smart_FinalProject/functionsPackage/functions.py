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

def decode(english, enchints):
    # Open the english file
    englishText = open(english,'r')
    # Open the hints file 
    hints = open(enchints)
    # Read the txt file
    readText = englishText.readlines()
    # Parse hints JSON
    parsed_json = json.load(hints)
    # Narrow JSON down to smart array
    smartJson = (parsed_json['Smart'])
    # Initialize array variable for formatted text
    formattedText = []
    # loop to replace new line character in txt file
    for sub in readText:
        formattedText.append(sub.replace("\n", ""))
    decodedHint = ''
    for num in smartJson:
        decodedHint += f"{formattedText[int(num)]} "        
    print(decodedHint)

