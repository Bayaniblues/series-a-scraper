from re import search
import nltk
import re

# added a higher order function for readability
mystring = ["CryptoKitties creator Dapper Labs raises $12 million for consumer-focused Flow blockchain",
            "Expert System raises $29.4 million for AI text extraction and analysis",
            'Thriver raises $33 million for virtual workplace wellness',
            "Google gives Android TV developers instant apps, speech-to-text, and predictive typing"]
def get_raise(data_in):
    for i,x in enumerate(data_in):
        mylist = re.split(r'\W+', x)
        if "raises" in mylist:
            raise_loc = mylist.index("raises")
            #print(x)
            #Searches for word "raises"

            # grabs the money
            money = mylist[raise_loc+1]
            money2 = mylist[raise_loc + 2]
            # gets the word raises, redundant
            raise_str = mylist[raise_loc]
            # finds the company name
            companyc = mylist[raise_loc-1]

            companyd = mylist[raise_loc - 2]
            companya = mylist[raise_loc - 3]
            print(companya+ " " +companyd + " " + companyc + " " + raise_str + " $" + money + " " + money2)
        else:
            pass

get_raise(mystring)
