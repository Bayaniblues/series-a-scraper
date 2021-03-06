import scrapy
from ..items import SeriesaItem
from re import search
import nltk
import re

# added a higher order function for readability
mystring = ["CryptoKitties creator Dapper Labs raises $12 million for consumer-focused Flow blockchain",
            "Expert System raises $29.4 million for AI text extraction and analysis"]
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
            print(companya+ " " + companyd + " " + companyc + " " + raise_str + " $" + money + " " + money2)
        else:
            pass

#get_raise(mystring)


noun_list = []
def find_nouns(data_in):
    for string in data_in:
        is_noun = lambda pos: pos[:2] == 'NN'
        tokenized = nltk.word_tokenize(string)
        nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
        noun_list.append(nouns)
    return noun_list

search_for = ['raises', 'funding']
data_store = []
def search_list(list_in, search_in,data_store):

    for index_x,x in enumerate(list_in):
        #print('index x is', index_x)

        for index_y,y in enumerate(search_in):
            #print('index y is', index_y)
            #print(x, '||', y)

            if search(list_in[index_x], search_in[index_y]):
                #print('is match')
                data_store.append(y)
            else:
                pass

    return data_store


class vbeat_spider(scrapy.Spider):
    #command with:
    #scrapy crawl vbeat
    name = "vbeat"

    start_urls = ['https://venturebeat.com/category/entrepreneur/']


    def parse(self, response):
        items = SeriesaItem()

        headline_items = response.css('.ArticleListing__title-link::text').extract()

        items['headline_name'] = headline_items

        print('======SEARCHING=====')
        run_this = list(find_nouns(search_list(search_for, headline_items, data_store)))
        print(get_raise(search_list(search_for, headline_items, data_store)))
        print('======END SEARCH=====')
        #yield items

