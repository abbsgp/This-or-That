# This Script will take a dictionary of words and convert them into a csv file
# Column 1 is the word
# Column 2 is the popularity of the word measured in uBreads
# Where 1 Bread is the peak realitive number of google searches
# of the term compared to the term bread in the last 12 months

from time import sleep
import pandas as pd                        
from pytrends.request import TrendReq
from urllib.request import Request, urlopen
import progressbar

def genDatabase(words):
    #store popularity in uBread
    refrenceWord = 'Bread'
    refrenceValue = 1000000
    pytrend = TrendReq()
    waitmultiplier = 0
    bar = progressbar.ProgressBar(max_value=len(words)).start()

    for i, word in enumerate(words):
        bar.update(i)
        kw_list = list();
        kw_list.append(refrenceWord)
        kw_list.append(word)
        successful = False
        while not successful:
            sleep(60*waitmultiplier)
            try:
                pytrend.build_payload(kw_list, timeframe='today 12-m')
                regiondf = pytrend.interest_by_region()
                regulator = refrenceValue/regiondf.loc["United States"][refrenceWord]
                regiondf.loc["United States"] *= regulator
                if waitmultiplier > 0: waitmultiplier -= 1
                successful = True;
            except Exception as e:
                waitmultiplier += 10
                print(e)
                print("word was: %s"%(word))
                print("cooling off for %d min"%(waitmultiplier))
        datafile = open("database.csv", "a")
        datafile.write("%s,%s\n"%(word,round(regiondf.loc["United States"][1])))
        datafile.close()
        #sleep(2)

url="https://raw.githubusercontent.com/isaacg1/words/master/common-nouns.txt"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()
webpage = web_byte.decode('utf-8')
worddict = webpage.split("\n")

genDatabase(worddict[0:len(worddict)])
