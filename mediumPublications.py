from medium import Client
from config import *
import webbrowser
import sys
import requests
from bs4 import BeautifulSoup
import requests

callback_url = "https://lucys-anime-server.herokuapp.com"

# Get articles from home page
def get_home_articles():
	r = requests.get("https://medium.com")
	data = r.text
	soup = BeautifulSoup(data,  "html.parser")

	# Featured articles
	posts = soup.find_all("div",{"class": "extremeHero-postContent"})
	links = soup.find_all("a", {"class":"ds-link"})
	for post in posts:
		title = post.find("div", {"class":"extremeHero-titleClamp"})
		byline = post.find("div", {"class":"extremeHero-byline"})
		print(title.text, byline.text)


if __name__ == '__main__':
	do_auth = False

	get_home_articles()

	if do_auth:

		# Go to http://medium.com/me/applications to get your application_id and application_secret.
		client = Client(application_id=MEDIUM_CLIENT_ID, application_secret=MEDIUM_CLIENT_SECRET)

		# Build the URL where you can send the user to obtain an authorization code.
		auth_url = client.get_authorization_url("secretstate", callback_url,
		                                        ["basicProfile", "publishPost", "listPublications"])

		# (Send the user to the authorization URL to obtain an authorization code.)
		print(auth_url)

		webbrowser.open(auth_url, new=2)

		print("Authorization code (at the end of the url that was just opened):")
		authorization_code = sys.stdin.readline().strip()

		# Exchange the authorization code for an access token.
		auth = client.exchange_authorization_code(authorization_code,
		                                          callback_url)

		# The access token is automatically set on the client for you after
		# a successful exchange, but if you already have a token, you can set it
		# directly.
		client.access_token = auth["access_token"]

		# Get profile details of the user identified by the access token.
		user = client.get_current_user()

		# Get publications
		publications = client._request("GET", "/v1/users/" + user["id"] + "/publications")
		print(publications)

# # Create a draft post.
# post = client.create_post(user_id=user["id"], title="Title", content="<h2>Title</h2><p>Content</p>",
#                           content_format="html", publish_status="draft")

# # When your access token expires, use the refresh token to get a new one.
# client.exchange_refresh_token(auth["refresh_token"])

# # Confirm everything went ok. post["url"] has the location of the created post.
# print("My new post!", post["url"])