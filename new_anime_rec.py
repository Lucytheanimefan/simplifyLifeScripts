'''
WHAT SHOULD YOU WATCH NEXT SEASON? (More like, what would Lucy watch next season?)
Warning: not accurate
How to use:
1. Download 
2. pip install the following modules: requests, bs4, textblob
3. Run: python -m textblob.download_corpora
4. Run: python new_anime_rec.py
'''

import subprocess
import sys
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob
import operator

aniChartUrl="https://www.livechart.me/"
great_studios = ["MAPPA","A-1 Pictures","Bones","Madhouse"]
good_studios = ["ufotable","Production I.G","Brains Base", "Shaft","Wit Studio"]
ok_studios = ["Lerche"]

bad_tags = ["School", "Harem","Ecchi", "Kids"]
sort_of_bad_tags = ["Slice of Life", "Comedy","Historical"]
ok_tags = ["Action","Drama","Fantasy","Shounen"] 
good_tags = ["Psychological","Seinen","Horror","Mystery","Thriller","Supernatural"]


def findSeasonRecs():
	season_anime = {}
	scores = {}
	print "Anime season (summer, spring, winter, or fall)"
	season = sys.stdin.readline().strip()
	print "year?"
	year = sys.stdin.readline().strip()
	url = aniChartUrl + season+"-"+year+"/tv"
	print(url)
	r = requests.get(url)
	data = r.text
	#print(data)
	soup = BeautifulSoup(data,  "html.parser")
	animez = soup.find_all("div", {"class": "anime-card"})
	for anime in animez:
		titlez = anime.find_all("h3",{"class":"main-title"})[0]
		title = titlez.text
		#print title
		scores[title] = 0 #each show starts off with 0

		########## check title ###########
		if "death" in title:
			scores[title]+=2

		########### check the tag ##########
		tags = [tag.text for tag in anime.find_all("ol",{"class":"anime-tags"})[0].find_all("li")]
		for tag in tags:
			if tag in good_tags:
				scores[title] += 6
			elif tag in sort_of_bad_tags:
				scores[title] += -3
			elif tag in bad_tags:
				scores[title] += -10
			elif tag in ok_tags:
				scores[title]+=2
		season_anime[title] = {"tags":tags}
		studios = anime.find_all("ul",{"class":"anime-studios"})

		############ check the studios #############
		parsed_studios = []
		for studio in studios:
			if studio.find_all("a"):
				stud = studio.find_all("a")[0].text
				if stud in great_studios:
					scores[title] += 6
				elif stud in good_studios:
					scores[title] += 3
				elif stud in ok_studios:
					scores[title] += 1
				parsed_studios.append(stud)
			else:
				parsed_studios.append(studio.find_all("li")[0].text)
		season_anime[title]["studios"]=parsed_studios

		############### check description ###################
	
		description = anime.find_all("div",{"class":"anime-synopsis"})[0].find("p").text
		if "death" in description:
			scores[title]+=2
		season_anime["description"] = description
		blob = TextBlob(description)
		for sentence in blob.sentences:
			#print(sentence.sentiment.polarity)
			scores[title]+=(-5*sentence.sentiment.polarity)
	
	#print season_anime
	sorted_anime = sorted(scores.items(), key=operator.itemgetter(1))
	i=0
	for anime in reversed(sorted_anime):
		i+=1
		print str(i) +": " + anime[0]+", "+str(anime[1])
	print("-------------")
	#print(season_anime)
	return sorted_anime



if __name__ == "__main__":
    findSeasonRecs()
