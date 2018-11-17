# Authors :
#  - Greg Woo
#  - Milo Sobral

import bs4 as bs
import urllib.request
import json
import sys

# sample call: python essai.py <LIEN AU HASARD D'UN ARTICLE>
#sauce = urllib.request.urlopen('https://www.washingtonpost.com/world/national-security/cia-concludes-saudi-crown-prince-ordered-jamal-khashoggis-assassination/2018/11/16/98c89fe6-e9b2-11e8-a939-9469f1166f9d_story.html?utm_term=.ddf51c68a5a2').read()
#print(sys.argv[1])

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
	d = {
		'id' : tit,
		'paragraph' : par
	}
	return d

# puts the dictionnary in a json file and create a file
def output_json(d) :
	j = json.dumps(d)
	f = open('current.json', 'w')
	print(j, file = f)
	f.close()
	return f

def main(url):
	soup = get_soup(url)
	file_name = output_json(parse_soup(soup))
	return file_name

if __name__ == "__main__" :
	main()
