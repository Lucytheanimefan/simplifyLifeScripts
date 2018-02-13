from bs4 import BeautifulSoup
import requests
import re
import json

anime_urls = ["http://typemoon.wikia.com/wiki/Shiki_Ryougi","http://ouran.wikia.com/wiki/Haruhi_Fujioka", "http://kamisamahajimemashita.wikia.com/wiki/Nanami_Momozono", "http://typemoon.wikia.com/wiki/Saber_(Fate/stay_night)", "http://ancientmagusbride.wikia.com/wiki/Chise_Hatori", "http://attackontitan.wikia.com/wiki/Mikasa_Ackerman","http://sangatsu-no-lion.wikia.com/wiki/Rei_Kiriyama", "http://horimiya.wikia.com/wiki/Hori_Kyouko", "http://horimiya.wikia.com/wiki/Miyamura_Izumi", "http://swordartonline.wikia.com/wiki/Yuuki_Asuna", "http://yahari.wikia.com/wiki/Yukino_Yukinoshita", "http://kaichouwamaidsama.wikia.com/wiki/Misaki_Ayuzawa", "http://tokyoghoul.wikia.com/wiki/Touka_Kirishima", "http://akatsukinoyona.wikia.com/wiki/Yona", "http://guiltycrown.wikia.com/wiki/Inori_Yuzuriha", "http://deathnote.wikia.com/wiki/Misa_Amane", "http://attackontitan.wikia.com/wiki/Historia_Reiss"]

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
			return_data["weight"] = label.findNext('div').text
		if "height" in label.text.lower():
			height = re.sub(r'\[.*\]', '', label.findNext('div').text)
			return_data["height"] = height

	if "weight" not in return_data or "height" not in return_data:
		td_labels = soup.find_all("td")
		for td in td_labels:
			#print td.text
			if "weight" in td.text.lower():
				return_data["weight"] = td.findNext('td').text
			if "height" in td.text.lower():
				return_data["height"] = td.findNext('td').text


	return return_data

def write_to_file(data, filename):
	with open(filename + '.txt', 'w') as outfile:
		json.dump(data, outfile)


if __name__ == '__main__':
	data = []
	for url in anime_urls:
		print url
		data.append(scrape_weight(url))
	write_to_file(data, "anime_character_stats")

