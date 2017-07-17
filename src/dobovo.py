import requests
from bs4 import BeautifulSoup
import csv
import json

#спарсить ссылки на города
#в каждом городе спарсить ссылки на страницы поискового запроса
# на каждой странице спарсить ссылки на объявление, тайтл, локацию, цену
# в каждом объявлении спарсить  календарь в виде "месяц - число - занято/цена"




def get_html(url):             # просто скачивает html по заданому url и возвращает в виде текста
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
	print('Current ID: ' + id)
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
	print(cities)
	for one_city in cities:
		print(one_city)
	print ("---------------||  Start Parse  ||---------------")
	for one_city in cities:
		print(one_city)
		city_total_pages = get_city_total_pages(get_html(one_city))
		for i in range(1,city_total_pages+1):
			print('!!!!!!!! page Number is: ' + str(i))
			some_page = one_city + '?page=' + str(i)
			get_page_data(get_html(some_page))








if __name__ == '__main__':
	main()