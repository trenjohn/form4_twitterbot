# -*- coding: utf-8 -*-

from twitter import *
import json
from time import sleep

token = "YOUR_TOKEN"
token_key = "YOUR_TOKEN_KEY"
con_secret_key = "YOUR_CONNECTION_SECRET_KEY"
con_secret = "YOUR_CONNECTION_SECRET"

t = Twitter(auth=OAuth(token, token_key, con_secret, con_secret_key))

with open('status_updates.json') as data_file:
    statuses = json.load(data_file)

for i in range (len(statuses)):
    status_update = statuses[i]["Status Update"]
        
    t.statuses.update(status=status_update)
    
    sleep(5.0)

