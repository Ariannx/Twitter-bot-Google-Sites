import credentials #credentials.py token and key (trabajo con un virtual env )
import requests #obvias razones
from twitter import OAuth, Twitter 
import time 

#xml = XML es un lenguaje que define los formatos aceptados que pueden utilizar los grupos para intercambiar información
#	entry content / p / class / divide / h1 //inspeccionar elemento 

from lxml.html import fromstring #necesito la estructura de arbol de la página web para acceder a todos los elementos.
import nltk # kit de herramientas de lenguaje natural, dividir párrafos de sitios web en oraciones.
nltk. download('punkt') #descarga un conjunto de datos necesario para analizar 
						#los párrafos y para formar parte de ellos (dividirlos) en componentes más pequeños.


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') #variable para dividir los párrafos y si es necesario en inglés

#librería para verificar nuestra cuenta de twitter que seamos propietarios.
oauth = OAuth(
    credentials.ACCESS_TOKEN,
    credentials.ACCESS_SECRET,
    credentials.CONSUMER_KEY,
    credentials.CONSUMER_SECRET
)
t = Twitter(auth=oauth) # variable a utilizar para dirigirnos a la autenticación 


def scrape_web():
	HEADERS = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
	        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
	    } # el sitio web me reconozca como un cliente genuino; solo es información acerca del sistema operativo 
	r = requests.get('https://sites.google.com/yachaytech.edu.ec/proyectos-universidad-yachay/', headers=HEADERS)
	#toma una URL y recupera la página web correspondiente.
	tree = fromstring(r.content) #leo el contenido dentro del sitio web en forma de arbol 
	link = tree.xpath('//div[@class="PsKE7e r8s4j-R6PoUb IKA38e baH5ib"]//div//a[@class="aJHbb dk90Ob hDrhEe HlqNPb"]/@href')
	#scrapear el contenido html
	links = ["https://sites.google.com"+x for x in link] #necesito una url abosluta, no relativa!!!! 
	#absoluta = servidor y ruta 
	#relativa = sin  las mencionadas, solo /yachaytech.edu.ec. bla bla


	for link in links:
		r = requests.get(link, headers=HEADERS)
		blog_tree = fromstring(r.content) #leo el contenido dentro del sitio web en forma de arbol
		parrafos = blog_tree.xpath('//div[@class="tyJCtd mGzaTb baZpAe"]/p[contains(text(), "")]/text()')
		#XPath es un lenguaje que permite construir expresiones que recorren y procesan un documento XML una dirección ?
		#parafos = blog_tree.xpath('//div[@class="tyJCtd mGzaTb baZpAe"]/p')
		#<Element at 0x21241bla bla> <Element at 0x343252 bla bla>
		#a =  [x.text_content() for x in paras if x.text_content()]
		#contenido = (a[0])
		#para_tokenized = tokenizer.tokenize(a)	
		contenido = [parrafos[0]] #solo quiero el primer párrafo
		#print(contenido) 
		str = ''.join(contenido) #tokenizer acepta str no list hago un solo string sin comillas ni listas tal y como está el párrafo
		parrafos_tokenized = tokenizer.tokenize(str) #separa el párrafo en string por elementos de una lista, cada elemento es una oracion

		#paras_text = [para.text_content() for para in paras if para.text_content()] #ya no es necesario
		#content = contenido.text_content() # ya no  necesario x2
		#para_tokenized = tokenizer.tokenize(contenido) #se cambia a la manera mía del bot 
		for sentence in range(10): #depende de cuántas proyectos están dentro de el sitio web puede ser 100 200 etc 
			text = (parrafos_tokenized[0])
			if text and 60<len(text)<210: #necesito una longitud para la oración a twittear, no puede excederse de los caracteres
				break
		else:
			yield None #No hay nada que twittear 
		yield '"%s" %s' % (text, link)
#no me sirve el print, necesito todas las iteraciones guardadas... 

def main():
	new_iter = []
	new_iter.append(globals()['scrape_web']()) #aplico global para un diccionario cada link con su respectivo párrafo.
	while True:
		for i, iterator in enumerate(new_iter): #que es enumerate ---- ? ----- 
			try: 	#utilizar print, however, no es lo que quiero, el código se queda igual... necesito todas las iteraciones
				tweet = next(iterator)
				t.statuses.update(status=tweet) #comando de la api de twitter, para twittear
				print(tweet, end='\n\n') #imprimo el twitter
				time.sleep(30) #podría ser menos pero el programa se confunde un poco...			
			except StopIteration: #el programa sigue funcionando hasta que encuentre un error de este índole
				new_iter[i] = globals()['scrape_web']() # cuando se vuelva a ejecutar el programa retoma el punto donde
														#se quedó, tratando de nuevo las iteraciones y botando
														# un tweet si es que hay nuevos, caso contrario
														#bota error de tipo stopiteration
main()
def raspberry():


