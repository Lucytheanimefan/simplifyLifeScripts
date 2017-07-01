import sys
from bs4 import BeautifulSoup
import requests 
import ast
import json
from multiprocessing import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

mal_url = "https://myanimelist.net/animelist/"


def get_anime_stream_site(anime_object):
	anime_url = anime_object["anime_url"]
	anime_title = anime_object["anime_title"]
	print anime_url
	to_return = {}
	ani_req = requests.get("https://myanimelist.net" + anime_url,verify=False)
	soup = BeautifulSoup(ani_req.text, "html.parser")

	# check for crunchyroll
	episodes = str(soup.find_all("ul", {"class":"anime-slide"}))
	if len(episodes)>0 and "crunchyroll" in episodes:
		to_return[anime_title] = ["crunchyroll"]
	
	# check for funimation
	funi = soup.find_all("a", {"title":"FUNimation Entertainment"})
	print funi
	if len(funi) > 0:
		if anime_title in to_return:
			to_return[anime_title].append("Funimation")
		else:
			to_return[anime_title] = "Funimation" 
	return to_return


def main():
    print("MAL username? ")
    username = sys.stdin.readline().strip()
    url = mal_url + username + "?status=6"
    r = requests.get(url, verify=False)
    data = r.text
    print r
    soup = BeautifulSoup(data,  "html.parser")
    plan_to_watch = json.loads(soup.find_all("table", {"class": "list-table"})[0]["data-items"])
    to_return = {}
    pool = Pool()                         # Create a multiprocessing Pool
    results = pool.map(get_anime_stream_site, plan_to_watch) 
    print results







if __name__ == '__main__':
    main()