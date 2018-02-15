from bs4 import BeautifulSoup
import requests
import re
import json
import urllib

anime_urls = ["http://typemoon.wikia.com/wiki/Shiki_Ryougi","http://ouran.wikia.com/wiki/Haruhi_Fujioka", "http://kamisamahajimemashita.wikia.com/wiki/Nanami_Momozono", "http://typemoon.wikia.com/wiki/Saber_(Fate/stay_night)", "http://ancientmagusbride.wikia.com/wiki/Chise_Hatori", "http://attackontitan.wikia.com/wiki/Mikasa_Ackerman","http://sangatsu-no-lion.wikia.com/wiki/Rei_Kiriyama", "http://horimiya.wikia.com/wiki/Hori_Kyouko", "http://horimiya.wikia.com/wiki/Miyamura_Izumi", "http://swordartonline.wikia.com/wiki/Yuuki_Asuna", "http://yahari.wikia.com/wiki/Yukino_Yukinoshita", "http://kaichouwamaidsama.wikia.com/wiki/Misaki_Ayuzawa", "http://tokyoghoul.wikia.com/wiki/Touka_Kirishima", "http://akatsukinoyona.wikia.com/wiki/Yona", "http://guiltycrown.wikia.com/wiki/Inori_Yuzuriha", "http://deathnote.wikia.com/wiki/Misa_Amane", "http://attackontitan.wikia.com/wiki/Historia_Reiss"]

characters = ['Shiki Ryougi', 'Haruhi Fujioka', 'Nanami Momozono', 'Saber', 'Rei Kiriyama', 'Mikasa Ackerman', 'Hori Kyouko', 'Miyamura_Izumi', 'Yuuki Asuna', 'Yukino_Yukinoshita', 'Misaki_Ayuzawa', 'Touka_Kirishima', 'Akatsuki no Yona Yona', 'Inori_Yuzuriha', 'Misa Amane', 'Historia Reiss', 'Chise Hatori', 'Izaya Orihara', 'Celty Sturluson', 'Rin Tousaka', 'Lawliet', 'Lelouch', 'Mitsuha','Ciel Phantomhive', 'Yuna Gasai', 'Nana', 'Shiro', 'Hiyori', 'Holo spice and wolf','Kaori Miyazono']

def find_anime_character_url(character_name):
	url = 'https://www.google.com/search?q=' + urllib.quote(character_name)
	print url
	r = requests.get(url)
	data = r.text
	soup = BeautifulSoup(data,  "html.parser")
	results = soup.find_all("a", href=True)
	#print results
	for link in results:
		if 'wikia' in link['href']: #/url?q=
			return link['href'][7:].split('&', 1)[0]
	
	return ''

def clean_data_string(data):
	regex = re.compile(".*?\((.*?)\)")
	return re.sub(r'\[.*\]', '', data).strip('\n')

def scrape_weight(url):
	regex = re.compile(".*?\((.*?)\)")
	r = requests.get(url)
	return_data = {}
	data = r.text
	soup = BeautifulSoup(data,  "html.parser")
	name = soup.find("h2", {"class": "pi-title"})
	if name is not None:
		return_data["name"] = name.text
	else:
		return_data["name"] = url.rsplit('/', 1)[-1]
	labels = soup.find_all("h3", {"class": "pi-data-label"})
	values = soup.find("div", {"class" : "pi-data-value"})
	for i, label in enumerate(labels):
		if "weight" in label.text.lower():
			return_data["weight"] = clean_data_string(label.findNext('div').text)#.strip('\n')
		if "height" in label.text.lower():
			height = clean_data_string(label.findNext('div').text)#re.sub(r'\[.*\]', '', label.findNext('div').text).strip('\n')
			return_data["height"] = height

	if "weight" not in return_data or "height" not in return_data:
		td_labels = soup.find_all("td")
		for td in td_labels:
			#print td.text
			if "weight" in td.text.lower():
				return_data["weight"] = clean_data_string(td.findNext('td').text.strip('\n'))
			if "height" in td.text.lower():
				return_data["height"] = clean_data_string(td.findNext('td').text)


	return return_data

def write_to_file(data, filename):
	with open(filename + '.txt', 'w') as outfile:
		json.dump(data, outfile)


if __name__ == '__main__':
	data = []
	for character in characters:
		url = find_anime_character_url(character)
		print url
		if url:
			data.append(scrape_weight(url))
	write_to_file(data, "anime_character_stats")
	# data = []
	# for url in anime_urls:
	# 	print url
	# 	data.append(scrape_weight(url))
	# write_to_file(data, "anime_character_stats")

