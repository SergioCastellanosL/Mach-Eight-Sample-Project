"""
Created on Wed Jan  5 12:24:34 2022

@author: Sergio Andrés Castellanos Landazábal
"""

#!/usr/bin/env python.

import json
import requests
from collections import defaultdict

def search(total):
    #Firstly download the dataset and save the data in the variable "players"
    response = requests.get("https://mach-eight.uc.r.appspot.com/")
    data = json.loads(response.text)
    NoPairs= 1
    players = data["values"]
    
    """
    Create the dictionary with the height as the keys and the players names 
    as the values.
    
    defaultdict is use to add keys to the dictionary.
    """
    HeightsDict = defaultdict(list)
    for player in players:
        HeightsDict[int(player['h_in'])].append(player['first_name'] + " " + 
                                                player['last_name'])
    
    """
    Finally, create loop to check the keys of the dictionary and find if there
    is some height that sum up to the total, and print the players names. 
    """
    for height in HeightsDict:
        if total - height in HeightsDict:
            NoPairs= 0
            for other in HeightsDict[total - height]:
                for player in HeightsDict[height]:
                    # This if is usufel to not print the same combination but 
                    # in another order
                    if player < other:
                        print('-'+ player +'   ' + other )
    
    return NoPairs

while(True):
    # cntrl-c to quit
    print('#####################################################')
    print('##             NBA Players Height APP              ##')
    print('##        Write exit to terminate the program      ##')
    print('#####################################################')
    print('Enter a number to look for all pairs of players whose')
    print('height in inches adds up to that integer')
    
    # Control the error when the user do not enter a number
    try:
        v = input('Enter the number: ')
        if v == 'exit':
            break
        total= int(v)
    except:
        print("Oops!")
        print("Try a number.")
        continue
    
    NoPairs= search(total)
    if NoPairs == 1:
        print('No matches found')
    print()