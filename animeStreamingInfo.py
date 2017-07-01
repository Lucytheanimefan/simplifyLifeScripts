import sys
from bs4 import BeautifulSoup
import requests 
import ast
import json
from multiprocessing import Pool
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

mal_url = "https://myanimelist.net/animelist/"


def get_anime_stream_site(anime_url):
	print anime_url
	ani_req = requests.get("https://myanimelist.net" + anime_url,verify=False)
	soup = BeautifulSoup(ani_req.text, "html.parser")
	if "crunchyroll" in soup.find_all("ul", {"class":"anime-slide"})[0]:
		to_return[anime["anime_title"]] = "crunchyroll"
		print to_return


def main():
    print("MAL username? ")
    username = sys.stdin.readline().strip()
    print(mal_url + username + "?status=6")
    r = requests.get(mal_url + username, verify=False)
    data = r.text
    soup = BeautifulSoup(data,  "html.parser")
    plan_to_watch = json.loads(soup.find_all("table", {"class": "list-table"})[0]["data-items"])
    to_return = {}
    anime_urls = [anime["anime_url"] for anime in plan_to_watch]
    pool = Pool()                         # Create a multiprocessing Pool
    pool.map(get_anime_stream_site, anime_urls) 
    

    print to_return






if __name__ == '__main__':
    main()