# -*- coding: utf-8 -*-

from twitter import *
import json
from datetime import datetime, timedelta
from time import sleep
from datetime import datetime, timedelta

now = datetime.now()

status_updates = []

with open('edgar.json') as data_file:
    results = json.load(data_file)

for i in range (len(results)):
    if (results[i]["Transactions"]):
        Company = results[i]["Company"]
        Ticker = results[i]["Ticker"]
    
        for p in range (len(results[i]["Transactions"])):
            Transaction = results[i]["Transactions"][p]
            
            transaction_type = Transaction["Transaction"]
            if (transaction_type == "S-Sale"):
                transaction_type_print = "sold"
            elif (transaction_type == "P-Purchase"):
                transaction_type_print = "bought"
            else:
                transaction_type_print = "transacted"
            
            shares_transacted = Transaction["Shares Transacted"]
            shares_transacted = shares_transacted.split('.')[0]
            
            first_name = Transaction["Name"].split()[1]
            last_name = Transaction["Name"].split()[0]
            
            link = Transaction["Link"]
            
            date = Transaction["Date"]
            month = date.split("-")[1]
            day = date.split("-")[2]
            date_object = datetime.strptime(date, '%Y-%m-%d')
            if (((now - date_object) == timedelta(days = 0))):
                date_to_print = "today"
            else:
                date_to_print = "on "+month+"/"+day
 
            #print Transaction
            status_update = "$"+Ticker+" "+first_name+" "+last_name+" "+transaction_type_print+" "+shares_transacted+" shares"+" "+date_to_print+". "+link
            
            final = {"Status Update": status_update}
            
            print status_update
            status_updates.append(final)
    

with open("status_updates.json", "w") as outfile:
    json.dump(status_updates, outfile)   
    

