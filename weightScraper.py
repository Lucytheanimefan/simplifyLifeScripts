from bs4 import BeautifulSoup
import requests
import re

anime_urls = ["http://typemoon.wikia.com/wiki/Shiki_Ryougi"]

def scrape_weight(url):
	regex = re.compile(".*?\((.*?)\)")
	r = requests.get(url)
	return_data = {}
	data = r.text
	soup = BeautifulSoup(data,  "html.parser")
	name = soup.find("h2", {"class": "pi-title"})
	return_data["name"] = name.text
	labels = soup.find_all("h3", {"class": "pi-data-label"})
	values = soup.find("div", {"class" : "pi-data-value"})
	for i, label in enumerate(labels):
		if "weight" in label.text.lower():
			return_data["weight"] = label.findNext('div').text
		if "height" in label.text.lower():
			height = re.sub(r'\[.*\]', '', label.findNext('div').text)
			return_data["height"] = height

	return return_data


if __name__ == '__main__':
	print scrape_weight("http://typemoon.wikia.com/wiki/Shiki_Ryougi")

