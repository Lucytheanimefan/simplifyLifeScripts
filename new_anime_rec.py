import subprocess
import sys
from bs4 import BeautifulSoup
import requests

aniChartUrl="https://www.livechart.me/"

def findSeasonRecs():
	season_anime = {}
	print "Anime season (summer, spring, winter, or fall)"
	season = sys.stdin.readline().strip()
	url = aniChartUrl + season+"-2017/tv"
	print(url)
	r = requests.get(url)
	data = r.text
	#print(data)
	soup = BeautifulSoup(data,  "html.parser")
	titles = soup.find_all("div", {"class": "anime-card"})
	for title in titles:
		alink = title.find_all("h3",{"class":"main-title"})[0]
		print(alink.text)
		tags = [tag.text for tag in title.find_all("ol",{"class":"anime-tags"})[0].find_all("li")]
		season_anime[alink.text] = {"tags":tags}
		studios = title.find_all("ul",{"class":"anime-studios"})
		#print(studios)
		parsed_studios = []
		for studio in studios:
			if studio.find_all("a"):
				stud = studio.find_all("a")[0].text
				parsed_studios.append(stud)
			else:
				parsed_studios.append(studio.find_all("li")[0].text)
		print(parsed_studios)



if __name__ == "__main__":
    findSeasonRecs()
