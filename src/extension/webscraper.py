import bs4 as bs
import urllib.request
import json
import sys

# sample call: python essai.py <LIEN AU HASARD D'UN ARTICLE>
#sauce = urllib.request.urlopen('https://www.washingtonpost.com/world/national-security/cia-concludes-saudi-crown-prince-ordered-jamal-khashoggis-assassination/2018/11/16/98c89fe6-e9b2-11e8-a939-9469f1166f9d_story.html?utm_term=.ddf51c68a5a2').read()
#print(sys.argv[1])

# retrieve url in sauce
# call beautifulsoup on soup to scrap text from website
sauce = urllib.request.urlopen(sys.argv[1]).read()
soup = bs.BeautifulSoup(sauce, 'lxml')

# loops are used to go through text and find a specific part of the html code
tit = ""
par = ""

for title in soup.find_all('h1'):
	#print (paragraph.text)
	tit += (title.text)

for para in soup.find_all('p'):
	#print (paragraph.text)
	par += (para.text)

#print (tit)
#print (par)

# putting everything in a dictionnary
d = {
	'id' : tit,
	'paragraph' : par
}

# puts the dictionnary in a json file and create a file
j = json.dumps(d)
f = open('sample.json', 'w')
print(j, file=f)
f.close()