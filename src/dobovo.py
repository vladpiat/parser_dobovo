import requests
from bs4 import BeautifulSoup
# import csv
import json






def get_html(url):             
	r = requests.get(url)
	return r.text

def check_outputfile():
	try:
		with open('dobovo.json', 'r') as inputfile:
			d = json.load(inputfile)
			if not(type(d) is list) :
				d = []
				#print('no list')
				with open('dobovo.json', 'w') as outfile:
	 				json.dump(d, outfile)

	except:
		#print('exept')
		with open('dobovo.json', 'w') as outfile:
			d = []
			json.dump(d, outfile)

def write_json(data):
	#datas = []
	with open('dobovo.json', 'r') as inputfile:
		d = json.load(inputfile)
		d.append(data)
		#print (type(d) is list)

		#print(d)	
	with open('dobovo.json', 'w') as outfile:
	 	json.dump(d, outfile)
		#outfile.write(json.dump(data))


def get_city_pages(html):
	soup = BeautifulSoup(html, 'lxml')
	city_pages = []
	url = 'https://www.dobovo.com'
	pages = soup.find('ul', class_='city-list__col').find_all('li', class_='dbv_price_round')
	for one_page in pages:
		city_pages.append(url + one_page.find('a').get('href'))

	return city_pages

def get_id(url):
	id = url.split('-')[-1].split('.')[0]
	# print('Current ID: ' + id)
	return id





def get_city_total_pages(html):
	soup = BeautifulSoup(html, 'lxml')
	try:
		pages = soup.find('div', class_='pages').find_all('a')[-1].get('href')
		total_pages = pages.split('=')[-1]
	except:
		total_pages = 1

	return int(total_pages)	


def get_schedule(id):
	schedule = requests.post('https://www.dobovo.com/dobovo/apt/ajax.php?action=getCalendar&lang=en', data={'id': id}).json()	
	####

	with open(id + '.json', 'w') as outfile:
	 	json.dump(schedule, outfile)

	####
	return schedule

def  get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	ads = soup.find('div', class_='catalog-wrap').find_all('div', class_='item')

	for ad in ads:

		

		
		try:
			title = ad.find('div', class_='item__main').find('a', class_='item__title').text.strip()
		except:
			title = ''


		try:
			url = ad.find('div', class_='item__main').find('a', class_='item__title').get('href')

			id = get_id(url)

			try:
				schedule = get_schedule(id)

			except:
				schedule = ''

		except:
			url = ''

		try:
			price = ad.find('div', class_='dbv_card_price').find('div', class_='dbv_apt_price_block').get('data-min-price').strip()
		except:
			price = ''

		#price = ad.find('div', class_='dbv_card_price').find('div', class_='dbv_apt_price_block').get('data-min-price').strip()
		#print(price)

		try:
			apartament_location = ad.find('div', class_='item__main').find('div', class_='item__address').text.strip()
			#print(metro)
		except:
			apartament_location = ''

		#print(ad.find('div', class_='item__main').find('div', class_='item__address').text.strip())

		data = {'title': title,
				'price': price,
				'apartament_location': apartament_location,
				'url': url,
				'id': id}#,
				#'schedule': schedule}

		write_json(data)

		








def main():
	url = 'https://www.dobovo.com/'
	check_outputfile()

	
	cities = get_city_pages(get_html(url))
	#print(cities)
	cities = ['https://www.dobovo.com/borispol-apartments.html', 'https://www.dobovo.com/malekhiv-apartments.html', 'https://www.dobovo.com/yuzhne-apartments.html', 'https://www.dobovo.com/mirgorod-apartments.html', 'https://www.dobovo.com/ismail-apartments.html', 'https://www.dobovo.com/bila-tserkva-apartments.html', 'https://www.dobovo.com/bucha-apartments.html', 'https://www.dobovo.com/yasinya-apartments.html', 'https://www.dobovo.com/skhidnytsia-apartments.html', 'https://www.dobovo.com/henichesk-apartments.html', 'https://www.dobovo.com/zatoka-apartments.html', 'https://www.dobovo.com/yatskovka-apartments.html', 'https://www.dobovo.com/brovary-apartments.html', 'https://www.dobovo.com/novoyavorivsk-apartments.html', 'https://www.dobovo.com/artemovsk-apartments.html', 'https://www.dobovo.com/kirovograd-apartments.html', 'https://www.dobovo.com/sergeyevka-apartments.html', 'https://www.dobovo.com/fontanka-apartments.html', 'https://www.dobovo.com/irpin-apartments.html', 'https://www.dobovo.com/kramatorsk-apartments.html', 'https://www.dobovo.com/nikopol-apartments.html', 'https://www.dobovo.com/melitopol-apartments.html', 'https://www.dobovo.com/koblevo-apartments.html', 'https://www.dobovo.com/mizhhirya-apartments.html', 'https://www.dobovo.com/svitiaz-apartments.html', 'https://www.dobovo.com/skadovsk-apartments.html', 'https://www.dobovo.com/vasylkiv-apartments.html', 'https://www.dobovo.com/lazurne-apartments.html', 'https://www.dobovo.com/pilipets-apartments.html', 'https://www.dobovo.com/vyshhorod-apartments.html', 'https://www.dobovo.com/kosiv-apartments.html', 'https://www.dobovo.com/kozyn-apartments.html', 'https://www.dobovo.com/gribovka-apartments.html', 'https://www.dobovo.com/nova-kakhovka-apartments.html', 'https://www.dobovo.com/karolino-buhaz-apartments.html', 'https://www.dobovo.com/dniprodzerzhynsk-apartments.html', 'https://www.dobovo.com/kriukivshchyna-apartments.html', 'https://www.dobovo.com/kanev-apartments.html', 'https://www.dobovo.com/tatariv-apartments.html', 'https://www.dobovo.com/stryi-apartments.html', 'https://www.dobovo.com/kryzhanivka-apartments.html', 'https://www.dobovo.com/kolomyia-apartments.html', 'https://www.dobovo.com/sinevirskaya-polyana-apartments.html', 'https://www.dobovo.com/rakhov-apartments.html', 'https://www.dobovo.com/izky-apartments.html', 'https://www.dobovo.com/yanoshi-apartments.html', 'https://www.dobovo.com/sloviansk-apartments.html', 'https://www.dobovo.com/oryavchyk-apartments.html', 'https://www.dobovo.com/polyanytsya-apartments.html', 'https://www.dobovo.com/mali-pidlisky-apartments.html', 'https://www.dobovo.com/zazymya-apartments.html', 'https://www.dobovo.com/skole-apartments.html', 'https://www.dobovo.com/boyarka-apartments.html', 'https://www.dobovo.com/primorskoe-apartments.html', 'https://www.dobovo.com/kostrina-apartments.html', 'https://www.dobovo.com/kobeliaky-apartments.html', 'https://www.dobovo.com/polyana-apartments.html', 'https://www.dobovo.com/staryi-saltiv-apartments.html', 'https://www.dobovo.com/verhovina-apartments.html', 'https://www.dobovo.com/obukhiv-apartments.html', 'https://www.dobovo.com/liubotyn-apartments.html', 'https://www.dobovo.com/zaliznyy-port-apartments.html', 'https://www.dobovo.com/vyshneve-apartments.html', 'https://www.dobovo.com/yablunytsya-apartments.html', 'https://www.dobovo.com/volovets-apartments.html', 'https://www.dobovo.com/kakhovka-apartments.html', 'https://www.dobovo.com/plavie-apartments.html', 'https://www.dobovo.com/pustomyty-apartments.html', 'https://www.dobovo.com/martove-apartments.html', 'https://www.dobovo.com/uman-apartments.html', 'https://www.dobovo.com/prymorsk-apartments.html', 'https://www.dobovo.com/balakliia-apartments.html', 'https://www.dobovo.com/chumaleve-apartments.html', 'https://www.dobovo.com/bilhorod-dnistrovskyi-apartments.html', 'https://www.dobovo.com/moscow-apartments.html', 'https://www.dobovo.com/saint-petersburg-apartments.html', 'https://www.dobovo.com/nizhnevartovsk-apartments.html', 'https://www.dobovo.com/ust-koksa-apartments.html', 'https://www.dobovo.com/surgut-apartments.html', 'https://www.dobovo.com/krasnodar-apartments.html', 'https://www.dobovo.com/ulan-ude-apartments.html', 'https://www.dobovo.com/sochi-apartments.html', 'https://www.dobovo.com/podolsk-apartments.html', 'https://www.dobovo.com/kursk-apartments.html', 'https://www.dobovo.com/tyumen-apartments.html', 'https://www.dobovo.com/stary-oskol-apartments.html', 'https://www.dobovo.com/kvartsitnyy-apartments.html', 'https://www.dobovo.com/krasnogorsk-apartments.html', 'https://www.dobovo.com/vyborg-apartments.html', 'https://www.dobovo.com/novgorod-apartments.html', 'https://www.dobovo.com/kazan-apartments.html', 'https://www.dobovo.com/suzdal-apartments.html', 'https://www.dobovo.com/tomsk-apartments.html', 'https://www.dobovo.com/kaliningrad-apartments.html', 'https://www.dobovo.com/kingisepp-apartments.html', 'https://www.dobovo.com/yaroslavl-apartments.html', 'https://www.dobovo.com/irkutsk-apartments.html', 'https://www.dobovo.com/novosibirsk-apartments.html', 'https://www.dobovo.com/ulyanovsk-apartments.html', 'https://www.dobovo.com/solnechnogorsk-apartments.html', 'https://www.dobovo.com/reutov-apartments.html', 'https://www.dobovo.com/chisinau-apartments.html', 'https://www.dobovo.com/belarus/minsk-apartments.html', 'https://www.dobovo.com/belarus/grodno-apartments.html', 'https://www.dobovo.com/belarus/mogilev-apartments.html', 'https://www.dobovo.com/tel-aviv-apartments.html', 'https://www.dobovo.com/bat-yam-apartments.html', 'https://www.dobovo.com/netanya-apartments.html', 'https://www.dobovo.com/istanbul-apartments.html', 'https://www.dobovo.com/ankara-apartments.html', 'https://www.dobovo.com/tbilisi-apartments.html', 'https://www.dobovo.com/batumi-apartments.html', 'https://www.dobovo.com/kvariati-apartments.html', 'https://www.dobovo.com/kvareli-apartments.html', 'https://www.dobovo.com/montreal-apartments.html', 'https://www.dobovo.com/krakow-apartments.html', 'https://www.dobovo.com/wroclaw-apartments.html', 'https://www.dobovo.com/katowice-apartments.html', 'https://www.dobovo.com/gallipoli-apartments.html', 'https://www.dobovo.com/marina-di-mancaversa-apartments.html', 'https://www.dobovo.com/taviano-apartments.html', 'https://www.dobovo.com/racale-apartments.html', 'https://www.dobovo.com/lecco-apartments.html', 'https://www.dobovo.com/verbania-apartments.html', 'https://www.dobovo.com/acquarica-del-capo-apartments.html', 'https://www.dobovo.com/milan-apartments.html', 'https://www.dobovo.com/stresa-apartments.html', 'https://www.dobovo.com/ugento-apartments.html', 'https://www.dobovo.com/torre-san-giovanni-apartments.html', 'https://www.dobovo.com/alliste-apartments.html', 'https://www.dobovo.com/lecce-apartments.html', 'https://www.dobovo.com/pescate-apartments.html', 'https://www.dobovo.com/capilungo-apartments.html', 'https://www.dobovo.com/pizzo-apartments.html', 'https://www.dobovo.com/lido-marini-apartments.html', 'https://www.dobovo.com/baveno-apartments.html', 'https://www.dobovo.com/torre-suda-apartments.html', 'https://www.dobovo.com/leuca-apartments.html', 'https://www.dobovo.com/positano-apartments.html', 'https://www.dobovo.com/melissano-apartments.html', 'https://www.dobovo.com/cortona-apartments.html', 'https://www.dobovo.com/oga-apartments.html', 'https://www.dobovo.com/tuglie-apartments.html', 'https://www.dobovo.com/palermo-apartments.html', 'https://www.dobovo.com/portoferraio-apartments.html', 'https://www.dobovo.com/parabita-apartments.html', 'https://www.dobovo.com/dervio-apartments.html', 'https://www.dobovo.com/porto-cesareo-apartments.html', 'https://www.dobovo.com/lesa-apartments.html', 'https://www.dobovo.com/pomigliano-darco-apartments.html', 'https://www.dobovo.com/posto-rosso-apartments.html', 'https://www.dobovo.com/bellagio-apartments.html', 'https://www.dobovo.com/florence-apartments.html', 'https://www.dobovo.com/pozzo-nuovo-paradiso-apartments.html', 'https://www.dobovo.com/arizzano-apartments.html', 'https://www.dobovo.com/borghetto-santo-spirito-apartments.html', 'https://www.dobovo.com/yerevan-apartments.html', 'https://www.dobovo.com/limassol-apartments.html', 'https://www.dobovo.com/larnaca-apartments.html', 'https://www.dobovo.com/famagusta-apartments.html', 'https://www.dobovo.com/marbella-apartments.html', 'https://www.dobovo.com/calella-apartments.html', 'https://www.dobovo.com/malaga-apartments.html', 'https://www.dobovo.com/castellar-de-valles-apartments.html', 'https://www.dobovo.com/cadaques-apartments.html', 'https://www.dobovo.com/neano-apartments.html', 'https://www.dobovo.com/barcelona-apartments.html', 'https://www.dobovo.com/riudarenes-apartments.html', 'https://www.dobovo.com/pineda-de-mar-apartments.html', 'https://www.dobovo.com/malpica-apartments.html', 'https://www.dobovo.com/lloret-de-mar-apartments.html', 'https://www.dobovo.com/blanes-apartments.html', 'https://www.dobovo.com/o-grove-apartments.html', 'https://www.dobovo.com/mijas-apartments.html', 'https://www.dobovo.com/talarn-apartments.html', 'https://www.dobovo.com/carballo-apartments.html', 'https://www.dobovo.com/el-vendrell-apartments.html', 'https://www.dobovo.com/a-coruna-apartments.html', 'https://www.dobovo.com/coma-ruga-apartments.html', 'https://www.dobovo.com/vidreres-apartments.html', 'https://www.dobovo.com/oleiros-apartments.html', 'https://www.dobovo.com/estepona-apartments.html', 'https://www.dobovo.com/girona-apartments.html', 'https://www.dobovo.com/bergondo-apartments.html', 'https://www.dobovo.com/cunit-apartments.html', 'https://www.dobovo.com/pontevedra-apartments.html', 'https://www.dobovo.com/san-pol-de-mar-apartments.html', 'https://www.dobovo.com/torrevieja-apartments.html', 'https://www.dobovo.com/poio-apartments.html', 'https://www.dobovo.com/la-caniza-apartments.html', 'https://www.dobovo.com/cee-apartments.html', 'https://www.dobovo.com/a-lanzada-apartments.html', 'https://www.dobovo.com/gondomar-apartments.html', 'https://www.dobovo.com/santa-cristina-daro-apartments.html', 'https://www.dobovo.com/sagaro-apartments.html', 'https://www.dobovo.com/marin-apartments.html', 'https://www.dobovo.com/creixell-apartments.html', 'https://www.dobovo.com/laxe-apartments.html', 'https://www.dobovo.com/sanxenxo-apartments.html', 'https://www.dobovo.com/sant-llorenc-savall-apartments.html', 'https://www.dobovo.com/redondela-apartments.html', 'https://www.dobovo.com/mino-apartments.html', 'https://www.dobovo.com/salobre-apartments.html', 'https://www.dobovo.com/vacarisses-apartments.html', 'https://www.dobovo.com/isla-de-arosa-apartments.html', 'https://www.dobovo.com/torredembarra-apartments.html', 'https://www.dobovo.com/torrelles-de-llobregat-apartments.html', 'https://www.dobovo.com/valverde-del-fresno-apartments.html', 'https://www.dobovo.com/sant-pere-de-vilamajor-apartments.html', 'https://www.dobovo.com/massanet-de-la-selva-apartments.html', 'https://www.dobovo.com/tordera-apartments.html', 'https://www.dobovo.com/silleda-apartments.html', 'https://www.dobovo.com/miami-platja-apartments.html', 'https://www.dobovo.com/vilafranca-del-penedes-apartments.html', 'https://www.dobovo.com/rodonya-apartments.html', 'https://www.dobovo.com/plasenzuela-apartments.html', 'https://www.dobovo.com/sant-cebria-de-vallalta-apartments.html', 'https://www.dobovo.com/santa-susanna-apartments.html', 'https://www.dobovo.com/santiago-de-compostela-apartments.html', 'https://www.dobovo.com/sabadell-apartments.html', 'https://www.dobovo.com/padron-apartments.html', 'https://www.dobovo.com/sils-apartments.html', 'https://www.dobovo.com/ayamonte-apartments.html', 'https://www.dobovo.com/ribeira-apartments.html', 'https://www.dobovo.com/tarragona-apartments.html', 'https://www.dobovo.com/vilagarcia-de-arousa-apartments.html', 'https://www.dobovo.com/sant-cugat-del-valles-apartments.html', 'https://www.dobovo.com/bienvenida-apartments.html', 'https://www.dobovo.com/canet-de-mar-apartments.html', 'https://www.dobovo.com/sort-apartments.html', 'https://www.dobovo.com/pobra-do-caraminal-apartments.html', 'https://www.dobovo.com/solsona-apartments.html', 'https://www.dobovo.com/salas-de-pallars-apartments.html', 'https://www.dobovo.com/tomino-apartments.html', 'https://www.dobovo.com/tossa-de-mar-apartments.html', 'https://www.dobovo.com/cedeira-apartments.html', 'https://www.dobovo.com/tremp-apartments.html', 'https://www.dobovo.com/terrassa-apartments.html', 'https://www.dobovo.com/riudellots-de-la-selva-apartments.html', 'https://www.dobovo.com/sada-apartments.html', 'https://www.dobovo.com/cuntis-apartments.html', 'https://www.dobovo.com/orista-apartments.html', 'https://www.dobovo.com/san-martin-sarroca-apartments.html', 'https://www.dobovo.com/xinzo-de-limia-apartments.html', 'https://www.dobovo.com/perafita-apartments.html', 'https://www.dobovo.com/colonia-sant-jordi-apartments.html', 'https://www.dobovo.com/les-avellanes-apartments.html', 'https://www.dobovo.com/sitges-apartments.html', 'https://www.dobovo.com/fuengirola-apartments.html', 'https://www.dobovo.com/carnota-apartments.html', 'https://www.dobovo.com/rota-apartments.html', 'https://www.dobovo.com/palleja-apartments.html', 'https://www.dobovo.com/montferri-apartments.html', 'https://www.dobovo.com/la-pobla-de-segur-apartments.html', 'https://www.dobovo.com/pinos-de-alhaurin-apartments.html', 'https://www.dobovo.com/moana-apartments.html', 'https://www.dobovo.com/bueu-apartments.html', 'https://www.dobovo.com/palma-de-mallorca-apartments.html', 'https://www.dobovo.com/forcarei-apartments.html', 'https://www.dobovo.com/puente-de-montanana-apartments.html', 'https://www.dobovo.com/sant-fost-de-campsentelles-apartments.html', 'https://www.dobovo.com/a-laracha-apartments.html', 'https://www.dobovo.com/camarinas-apartments.html', 'https://www.dobovo.com/cellers-apartments.html', 'https://www.dobovo.com/la-llacuna-apartments.html', 'https://www.dobovo.com/mijas-costa-apartments.html', 'https://www.dobovo.com/arbucies-apartments.html', 'https://www.dobovo.com/sigueiro-apartments.html', 'https://www.dobovo.com/castellbell-i-el-vilar-apartments.html', 'https://www.dobovo.com/cubells-apartments.html', 'https://www.dobovo.com/pinofranqueado-apartments.html', 'https://www.dobovo.com/magacela-apartments.html', 'https://www.dobovo.com/san-pedro-de-riudevitlles-apartments.html', 'https://www.dobovo.com/fisterra-apartments.html', 'https://www.dobovo.com/berga-apartments.html', 'https://www.dobovo.com/a-touza-apartments.html', 'https://www.dobovo.com/barbera-del-valles-apartments.html', 'https://www.dobovo.com/cambrils-apartments.html', 'https://www.dobovo.com/valdecilla-apartments.html', 'https://www.dobovo.com/vimianzo-apartments.html', 'https://www.dobovo.com/bellaterra-apartments.html', 'https://www.dobovo.com/morana-apartments.html', 'https://www.dobovo.com/caldes-d-estrac-apartments.html', 'https://www.dobovo.com/noalla-apartments.html', 'https://www.dobovo.com/altafulla-apartments.html', 'https://www.dobovo.com/torre-de-cabdella-apartments.html', 'https://www.dobovo.com/meloneras-apartments.html', 'https://www.dobovo.com/riudoms-apartments.html', 'https://www.dobovo.com/puentedeume-apartments.html', 'https://www.dobovo.com/brion-apartments.html', 'https://www.dobovo.com/la-selva-del-camp-apartments.html', 'https://www.dobovo.com/figueres-apartments.html', 'https://www.dobovo.com/foz-apartments.html', 'https://www.dobovo.com/bellvei-del-penedes-apartments.html', 'https://www.dobovo.com/monistrol-de-montserrat-apartments.html', 'https://www.dobovo.com/valdovino-apartments.html', 'https://www.dobovo.com/tamarit-apartments.html', 'https://www.dobovo.com/san-celoni-apartments.html', 'https://www.dobovo.com/salou-apartments.html', 'https://www.dobovo.com/platja-daro-apartments.html', 'https://www.dobovo.com/banyeres-del-penedes-apartments.html', 'https://www.dobovo.com/santa-cruz-de-tenerife-apartments.html', 'https://www.dobovo.com/hio-apartments.html', 'https://www.dobovo.com/cabrera-de-mar-apartments.html', 'https://www.dobovo.com/ares-apartments.html', 'https://www.dobovo.com/navas-apartments.html', 'https://www.dobovo.com/xerta-apartments.html', 'https://www.dobovo.com/nerja-apartments.html', 'https://www.dobovo.com/vilassar-de-mar-apartments.html', 'https://www.dobovo.com/monesterio-apartments.html', 'https://www.dobovo.com/ferrol-apartments.html', 'https://www.dobovo.com/alcover-apartments.html', 'https://www.dobovo.com/muros-apartments.html', 'https://www.dobovo.com/olujas-apartments.html', 'https://www.dobovo.com/ses-salines-apartments.html', 'https://www.dobovo.com/corralejo-apartments.html', 'https://www.dobovo.com/la-garriga-apartments.html', 'https://www.dobovo.com/muxia-apartments.html', 'https://www.dobovo.com/el-pla-del-penedes-apartments.html', 'https://www.dobovo.com/chiclana-de-la-frontera-apartments.html', 'https://www.dobovo.com/a-veneira-de-roques-apartments.html', 'https://www.dobovo.com/rivert--apartments.html', 'https://www.dobovo.com/cambados-apartments.html', 'https://www.dobovo.com/abrera-apartments.html', 'https://www.dobovo.com/ibiza-town-apartments.html', 'https://www.dobovo.com/pobra-do-brollon-apartments.html', 'https://www.dobovo.com/quarteira-apartments.html', 'https://www.dobovo.com/albufeira-apartments.html', 'https://www.dobovo.com/setubal-apartments.html', 'https://www.dobovo.com/canico-apartments.html', 'https://www.dobovo.com/lisbon-apartments.html', 'https://www.dobovo.com/pinhao-apartments.html', 'https://www.dobovo.com/loule-apartments.html', 'https://www.dobovo.com/baku-apartments.html', 'https://www.dobovo.com/gagra-apartments.html', 'https://www.dobovo.com/saint-pauls-bay-apartments.html', 'https://www.dobovo.com/sliema-apartments.html', 'https://www.dobovo.com/st-julians-apartments.html', 'https://www.dobovo.com/tallinn-apartments.html', 'https://www.dobovo.com/astana-apartments.html', 'https://www.dobovo.com/almaty-apartments.html', 'https://www.dobovo.com/acharavi-apartments.html', 'https://www.dobovo.com/korissia-apartments.html', 'https://www.dobovo.com/prague-apartments.html', 'https://www.dobovo.com/koh-chang-apartments.html', 'https://www.dobovo.com/berlin-apartments.html', 'https://www.dobovo.com/cologne-apartments.html', 'https://www.dobovo.com/pamporovo-apartments.html', 'https://www.dobovo.com/copenhagen-apartments.html', 'https://www.dobovo.com/cannes-apartments.html', 'https://www.dobovo.com/biarritz-apartments.html', 'https://www.dobovo.com/aigues-mortes-apartments.html', 'https://www.dobovo.com/antibes-apartments.html', 'https://www.dobovo.com/megeve-apartments.html', 'https://www.dobovo.com/marseille-apartments.html', 'https://www.dobovo.com/montpellier-apartments.html', 'https://www.dobovo.com/primosten-apartments.html', 'https://www.dobovo.com/crikvenica-apartments.html', 'https://www.dobovo.com/rovinj-apartments.html', 'https://www.dobovo.com/stockholm-apartments.html', 'https://www.dobovo.com/guelmim-apartments.html', 'https://www.dobovo.com/vienna-apartments.html', 'https://www.dobovo.com/hallstatt-apartments.html', 'https://www.dobovo.com/zurich-apartments.html']
	# for one_city in cities:
	# 	print(one_city)
	# print ("---------------||  Start Parse  ||---------------")
	for one_city in cities:
		# print(one_city)
		city_total_pages = get_city_total_pages(get_html(one_city))
		for i in range(1,city_total_pages+1):
			#print('!!!!!!!! page Number is: ' + str(i))
			some_page = one_city + '?page=' + str(i)
			get_page_data(get_html(some_page))








if __name__ == '__main__':
	main()