import credentials
import requests
from twitter import OAuth, Twitter 
import time 
from lxml.html import fromstring 
import nltk

nltk. download('punkt') #Ejecutar sólo en la primera prueba, luego se puede comentar por lo que ya estará descargado el kit 

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
oauth = OAuth(
    credentials.ACCESS_TOKEN,
    credentials.ACCESS_SECRET,
    credentials.CONSUMER_KEY,
    credentials.CONSUMER_SECRET
)
t = Twitter(auth=oauth) 

def scrape_web():
	HEADERS = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
	        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	    	} 
	r = requests.get('https://sites.google.com/yachaytech.edu.ec/proyectos-universidad-yachay/', headers=HEADERS)
	tree = fromstring(r.content) 
	link = tree.xpath('//div[@class="PsKE7e r8s4j-R6PoUb IKA38e baH5ib"]//div//a[@class="aJHbb dk90Ob hDrhEe HlqNPb"]/@href')
	links = ["https://sites.google.com"+x for x in link] 
	
	for link in links:
		r = requests.get(link, headers=HEADERS)
		blog_tree = fromstring(r.content) 
		parrafos = blog_tree.xpath('//div[@class="tyJCtd mGzaTb baZpAe"]/p[contains(text(), "")]/text()')
		contenido = [parrafos[0]] 
		str = ''.join(contenido) 
		parrafos_tokenized = tokenizer.tokenize(str) 
		for sentence in range(10): 
			text = (parrafos_tokenized[0])
			if text and 60<len(text)<210: 
				break
		else:
			yield " "
		yield '"%s" %s' % (text, link) 

def main():
	new_iter = []
	new_iter.append(globals()['scrape_web']()) 
	while True:
		for i, iterator in enumerate(new_iter): 
			try: 	
				tweet = next(iterator)
				t.statuses.update(status=tweet) 
				print(tweet, end='\n\n') 
				time.sleep(30) 			
			except StopIteration: 
				new_iter[i] = globals()['scrape_web']() 
main()


