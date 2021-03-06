# label data in [data] folders
# author: Zoe Lapomme
import os
from os import listdir
from os.path import isfile, join

def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data")
    return filename

#method to return dictionary with json file name as key and reliability rating as value
def getReliability (files) :

    #create dictionary
    reliability = {}

    #add each file with corresponding reliability
    for s in files :
        if s == "abc-news-au.json" :
            reliability [s] = 6
        elif s == "abc-news.json" :
            reliability [s] = 6
        elif s == "al-jazeera-english.json" :
            reliability [s] = 6
        elif s == "ars-technica.json" :
            reliability [s] = 6
        elif s == "associated-press.json" :
            reliability [s] = 9
        elif s == "australian-financial-review.json" :
            reliability [s] = 6
        elif s == "axios.json" :
            reliability [s] = 8
        elif s == "bbc-news.json" :
            reliability [s] = 9
        elif s == "bbc-sport.json" :
            reliability [s] = 8
        elif s == "bleacher-report.json" :
            reliability [s] = 4
        elif s == "bloomberg.json" :
            reliability [s] = 7
        elif s == "breitbart-news.json" :
            reliability [s] = 1
        elif s == "business-insider-uk.json" :
            reliability [s] = 5
        elif s == "business-insider.json" :
            reliability [s] = 6
        elif s == "buzzfeed.json" :
            reliability [s] = 3
        elif s == "cbc-news.json" :
            reliability [s] = 7
        elif s == "cbs-news.json" :
            reliability [s] = 7
        elif s == "cnbc.json" :
            reliability [s] = 7
        elif s == "cnn-es.json" :
            reliability [s] = 4
        elif s == "cnn.json" :
            reliability [s] = 5
        elif s == "crypto-coins-news.json" :
            reliability [s] = 2
        elif s == "daily-mail.json" :
            reliability [s] = 3
        elif s == "engadget.json" :
            reliability [s] = 5
        elif s == "entertainment-weekly.json" :
            reliability [s] = 3
        elif s == "espn-cric-info.json" :
            reliability [s] = 6
        elif s == "espn.json" :
            reliability [s] = 7
        elif s == "financial-post.json" :
            reliability [s] = 7
        elif s == "financial-times.json" :
            reliability [s] = 7
        elif s == "fortune.json" :
            reliability [s] = 5
        elif s == "four-four-two.json" :
            reliability [s] = 2
        elif s == "fox-news.json" :
            reliability [s] = 2
        elif s == "fox-sports.json" :
            reliability [s] = 4
        elif s == "google-news-au.json" :
            reliability [s] = 4
        elif s == "google-news-ca.json" :
            reliability [s] = 4
        elif s == "google-news-uk.json" :
            reliability [s] = 4
        elif s == "google-news.json" :
            reliability [s] = 4
        elif s == "hacker-news.json" :
            reliability [s] = 5
        elif s == "ign.json" :
            reliability [s] = 5
        elif s == "independent.json" :
            reliability [s] = 7
        elif s == "mashable.json" :
            reliability [s] = 3
        elif s == "medical-news-today.json" :
            reliability [s] = 7
        elif s == "metro.json" :
            reliability [s] = 4
        elif s == "mirror.json" :
            reliability [s] = 3
        elif s == "msnbc.json" :
            reliability [s] = 2
        elif s == "mtv-news-uk.json" :
            reliability [s] = 1
        elif s == "mtv-news.json" :
            reliability [s] = 2
        elif s == "national-geographic.json" :
            reliability [s] = 7
        elif s == "national-review.json" :
            reliability [s] = 3
        elif s == "nbc-news.json" :
            reliability [s] = 7
        elif s == "new-scientist.json" :
            reliability [s] = 4
        elif s == "new-york-magazine.json" :
            reliability [s] = 4
        elif s == "news-com-au.json" :
            reliability [s] = 2
        elif s == "newsweek.json" :
            reliability [s] = 7
        elif s == "next-big-future.json" :
            reliability [s] = 5
        elif s == "nfl-news.json" :
            reliability [s] = 5
        elif s == "nhl-news.json" :
            reliability [s] = 6
        elif s == "politico.json" :
            reliability [s] = 8
        elif s == "polygon.json" :
            reliability [s] = 3
        elif s == "recode.json" :
            reliability [s] = 5
        elif s == "reddit-r-all.json" :
            reliability [s] = 1
        elif s == "reuters.json" :
            reliability [s] = 9
        elif s == "talksport.json" :
            reliability [s] = 3
        elif s == "techcrunch.json" :
            reliability [s] = 6
        elif s == "techradar.json" :
            reliability [s] = 3
        elif s == "the-american-conservative.json" :
            reliability [s] = 0
        elif s == "the-economist.json" :
            reliability [s] = 9
        elif s == "the-globe-and-mail.json" :
            reliability [s] = 8
        elif s == "the-guardian-au.json" :
            reliability [s] = 8
        elif s == "the-guardian-uk.json" :
            reliability [s] = 8
        elif s == "the-hill.json" :
            reliability [s] = 8
        elif s == "the-huffington-post.json" :
            reliability [s] = 3
        elif s == "the-lad-bible.json" :
            reliability [s] = 1
        elif s == "the-new-york-times.json" :
            reliability [s] = 8
        elif s == "the-next-web.json" :
            reliability [s] = 4
        elif s == "the-sport-bible.json" :
            reliability [s] = 0
        elif s == "the-telegraph.json" :
            reliability [s] = 6
        elif s == "the-verge.json" :
            reliability [s] = 6
        elif s == "the-wall-street-journal.json" :
            reliability [s] = 8
        elif s == "the-washington-post.json" :
            reliability [s] = 8
        elif s == "the-washington-times.json" :
            reliability [s] = 3
        elif s == "time.json" :
            reliability [s] = 8
        elif s == "usa-today.json" :
            reliability [s] = 7
        elif s == "vice-news.json" :
            reliability [s] = 5
        elif s == "wired.json" :
            reliability [s] = 4

    return reliability

#method to return dictionary with json file name as key and bias rating as value
def getBias (files) :

    #create dictionary
    bias = {}

    #add each file with corresponding bias
    for s in files :
        if s == "abc-news-au.json" :
            bias [s] = 1
        elif s == "abc-news.json" :
            bias [s] = 1
        elif s == "al-jazeera-english.json" :
            bias [s] = 2
        elif s == "ars-technica.json" :
            bias [s] = 0
        elif s == "associated-press.json" :
            bias [s] = 1
        elif s == "australian-financial-review.json" :
            bias [s] = 0
        elif s == "axios.json" :
            bias [s] = 1
        elif s == "bbc-news.json" :
            bias [s] = 1
        elif s == "bbc-sport.json" :
            bias [s] = 0
        elif s == "bleacher-report.json" :
            bias [s] = 0
        elif s == "bloomberg.json" :
            bias [s] = 1
        elif s == "breitbart-news.json" :
            bias [s] = 4
        elif s == "business-insider-uk.json" :
            bias [s] = 0
        elif s == "business-insider.json" :
            bias [s] = 0
        elif s == "buzzfeed.json" :
            bias [s] = 3
        elif s == "cbc-news.json" :
            bias [s] = 1
        elif s == "cbs-news.json" :
            bias [s] = 1
        elif s == "cnbc.json" :
            bias [s] = 1
        elif s == "cnn-es.json" :
            bias [s] = 3
        elif s == "cnn.json" :
            bias [s] = 3
        elif s == "crypto-coins-news.json" :
            bias [s] = 0
        elif s == "daily-mail.json" :
            bias [s] = 1
        elif s == "engadget.json" :
            bias [s] = 0
        elif s == "entertainment-weekly.json" :
            bias [s] = 0
        elif s == "espn-cric-info.json" :
            bias [s] = 0
        elif s == "espn.json" :
            bias [s] = 0
        elif s == "financial-post.json" :
            bias [s] = 2
        elif s == "financial-times.json" :
            bias [s] = 2
        elif s == "fortune.json" :
            bias [s] = 0
        elif s == "four-four-two.json" :
            bias [s] = 0
        elif s == "fox-news.json" :
            bias [s] = 4
        elif s == "fox-sports.json" :
            bias [s] = 0
        elif s == "google-news-au.json" :
            bias [s] = 0
        elif s == "google-news-ca.json" :
            bias [s] = 0
        elif s == "google-news-uk.json" :
            bias [s] = 0
        elif s == "google-news.json" :
            bias [s] = 0
        elif s == "hacker-news.json" :
            bias [s] = 0
        elif s == "ign.json" :
            bias [s] = 0
        elif s == "independent.json" :
            bias [s] = 2
        elif s == "mashable.json" :
            bias [s] = 0
        elif s == "medical-news-today.json" :
            bias [s] = 0
        elif s == "metro.json" :
            bias [s] = 0
        elif s == "mirror.json" :
            bias [s] = 0
        elif s == "msnbc.json" :
            bias [s] = 2
        elif s == "mtv-news-uk.json" :
            bias [s] = 0
        elif s == "mtv-news.json" :
            bias [s] = 0
        elif s == "national-geographic.json" :
            bias [s] = 0
        elif s == "national-review.json" :
            bias [s] = 2
        elif s == "nbc-news.json" :
            bias [s] = 1
        elif s == "new-scientist.json" :
            bias [s] = 0
        elif s == "new-york-magazine.json" :
            bias [s] = 1
        elif s == "news-com-au.json" :
            bias [s] = 0
        elif s == "newsweek.json" :
            bias [s] = 0
        elif s == "next-big-future.json" :
            bias [s] = 0
        elif s == "nfl-news.json" :
            bias [s] = 0
        elif s == "nhl-news.json" :
            bias [s] = 0
        elif s == "politico.json" :
            bias [s] = 2
        elif s == "polygon.json" :
            bias [s] = 0
        elif s == "recode.json" :
            bias [s] = 0
        elif s == "reddit-r-all.json" :
            bias [s] = 0
        elif s == "reuters.json" :
            bias [s] = 1
        elif s == "talksport.json" :
            bias [s] = 0
        elif s == "techcrunch.json" :
            bias [s] = 0
        elif s == "techradar.json" :
            bias [s] = 0
        elif s == "the-american-conservative.json" :
            bias [s] = 3
        elif s == "the-economist.json" :
            bias [s] = 2
        elif s == "the-globe-and-mail.json" :
            bias [s] = 1
        elif s == "the-guardian-au.json" :
            bias [s] = 2
        elif s == "the-guardian-uk.json" :
            bias [s] = 2
        elif s == "the-hill.json" :
            bias [s] = 1
        elif s == "the-huffington-post.json" :
            bias [s] = 3
        elif s == "the-lad-bible.json" :
            bias [s] = 0
        elif s == "the-new-york-times.json" :
            bias [s] = 1
        elif s == "the-next-web.json" :
            bias [s] = 0
        elif s == "the-sport-bible.json" :
            bias [s] = 0
        elif s == "the-telegraph.json" :
            bias [s] = 0
        elif s == "the-verge.json" :
            bias [s] = 0
        elif s == "the-wall-street-journal.json" :
            bias [s] = 1
        elif s == "the-washington-post.json" :
            bias [s] = 1
        elif s == "the-washington-times.json" :
            bias [s] = 2
        elif s == "time.json" :
            bias [s] = 1
        elif s == "usa-today.json" :
            bias [s] = 1
        elif s == "vice-news.json" :
            bias [s] = 0
        elif s == "wired.json" :
            bias [s] = 0

    return bias

def main () :
    mypath = get_data_file()
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    rel = getReliability(files)
    bias = getBias(files)
    print(rel)
    print(bias)

if __name__ == "__main__" :
    main()
