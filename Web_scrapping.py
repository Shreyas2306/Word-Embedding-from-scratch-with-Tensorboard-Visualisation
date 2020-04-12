#Importing Libraries

import requests
from scrapy import Selector
import pickle


#class to extracting text data using Web Scraping
class WebScraping:
    def __init__(self, path):
        self.path = path 

    #Importing URLs
    def Extracting_urls(self):
         
        with open ('outfile', 'rb') as fp:
            self.urls = pickle.load(fp)

    def Extracting_data(self):

        #list to store data
        text = []
        #list to store data as a single list
        self.new_text = []
        
        #loop to extract data
        
        for url in self.urls:

            html = requests.get(url).content
            sel = Selector(text = html)
            info = sel.css('p::text').extract()

            text.append(info)
        
        #storing data from list of list as single list
        self.new_text = [' '.join(s) for s in text]
        
    def Preprocess_data(self):

        text1 = [s.replace('\t','') for s in self.new_text]
        text2 = [s.replace('\n','') for s in text1]
        self.str_list = list(filter(None, text2))    

    def save_file(self, path):
        self.path = path
        with open(self.path, 'w') as f:

            for item in self.str_list:
                  f.write(item)

webscraping = WebScraping(path = './URLs.txt')
webscraping.Extracting_urls()
webscraping.Extracting_data()
webscraping.Preprocess_data()
webscraping.save_file(path = './Document.txt')