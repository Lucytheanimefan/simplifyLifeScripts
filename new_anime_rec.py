import subprocess
import sys
from bs4 import BeautifulSoup
import requests

aniChartUrl="https://www.livechart.me/"

def findSeasonRecs():
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
		alink = title.find_all("h3",{"class":"main-title"})
		for link in alink:
			print link.text



if __name__ == "__main__":
    findSeasonRecs()
