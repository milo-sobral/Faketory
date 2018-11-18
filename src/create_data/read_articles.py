import json
import os
import bs4 as bs
import urllib.request
from os import listdir
from os.path import isfile, join


def get_data_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data2")
    return filename


def get_output_file() :
    current_dir = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(current_dir, "../..", "data3")
    return filename

# retrieve url in sauce
# call beautifulsoup on soup to scrap text from website
def get_soup(url) :
	sauce = urllib.request.urlopen(url).read()
	soup = bs.BeautifulSoup(sauce, 'lxml')
	return soup

# parse test from source and return disctionary with info
def parse_soup(soup) :
	tit = ""
	par = ""
	for title in soup.find_all('h1'):
		tit += (title.text)
	for para in soup.find_all('p'):
		par += (para.text)
	# putting everything in a dictionnary
	d = dict(id = tit, paragraph = par)
	return d

# puts the dictionnary in a json file and create a file
def output_json(d, source, counter):
    j = json.dumps(d)
    data_path = os.path.join(get_output_file(), source, source + str(counter) + '.json')
    with open((data_path), 'w') as fp:
        json.dump(d, fp)

def parse_one_article(url, source, counter):
	soup = get_soup(url)
	d = parse_soup(soup)
	output_json(d, source, counter)

def parse_one_source(urls, source) :
    counter = 0
    directory = os.path.join(get_output_file(), source)
    try:
        os.stat(directory)
    except:
        os.mkdir(directory)
    for url in urls:
        parse_one_article(url, source, counter)
        counter += 1
        print("working on article #{}".format(counter))
    counter = 0

def parse_library():
    lib_path = get_data_file()
    print(lib_path)
    onlyfiles = [f for f in listdir(lib_path) if isfile(join(lib_path, f))]
    # print(onlyfiles)
    for file in onlyfiles :
        print("printing file {}".format(file))
        with open(os.path.join(lib_path, file)) as json_data:
            d = json.load(json_data)
        list_urls = d['urls']
        parse_one_source(list_urls, d['source'])

if __name__ == "__main__" :
	parse_library()
