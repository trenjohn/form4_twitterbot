from bs4 import BeautifulSoup
from requests import get
import json
from datetime import datetime, timedelta
from time import sleep

url = "https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK="

with open('CIK_list.json') as data_file:
    CIK_list = json.load(data_file)
    
results = []

for i in range (len(CIK_list)):
    Company = CIK_list[i]["Company"]
    Ticker = CIK_list[i]["Ticker"]
    CIK = CIK_list[i]["CIK"]

    full_url = url + CIK
    
    print "Searching: " + full_url + " ("+Ticker+")" 

    soup = BeautifulSoup(get(full_url).content, "lxml")
    
    hit = []
    now = datetime.now()

    table = soup.find("table", {"id":"transaction-report"})
    rows = table.findAll("tr")

    for row in rows:
        data_columns = row.find_all("td")
        for data in data_columns:
            if (data.get_text() == "S-Sale" or data.get_text() == "P-Purchase"):
                target = row.find_all("td")
                date = target[1].get_text()
                date_object = datetime.strptime(date, '%Y-%m-%d')
                if (((now - date_object) <= timedelta(days = 2)) and ((now - date_object) > timedelta(days = -1))):
                    date = target[1].get_text()    
                    name = target[3].get_text()
                    partial_link = target[4].find("a").get('href')
                    link = "https://www.sec.gov" + partial_link
                    transaction = target[5].get_text()
                    ownership = target[6].get_text()
                    shares_transacted = target[7].get_text()
                    shares_owned = target[8].get_text()

                    item = {'Date': date, 'Name': name, 'Link': link, 'Transaction': transaction, 'Ownership': ownership, 'Shares Transacted': shares_transacted, 'Shares Owned': shares_owned}
                    
                    print item
                    
                    hit.append(item)
    
    company_hits = {"Company": Company, "Ticker": Ticker, "Transactions": hit}   
    
    results.append(company_hits)
    
    
        
    sleep(0.1)
            
with open("edgar.json", "w") as outfile:
    json.dump(results, outfile)
    
print results