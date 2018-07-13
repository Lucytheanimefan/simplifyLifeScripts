from medium import Client
import webbrowser
import sys
import json
import requests
from fake_useragent import UserAgent
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from settings import *

callback_url = "https://lucys-anime-server.herokuapp.com"

ua = UserAgent()

PRIVATE_API_URL = "https://medium.com/_/api"

ME_URL = "https://medium.com/me"

def post_url(post_id):
    return PRIVATE_API_URL + "/posts/" + post_id + "/"

def post_responses_url(post_id, filter_args="best"):
    return post_url(post_id) + "responses?filter=" + filter_args

def topic_subscription_url(topic):
    return ME_URL + "/subscriptions/topic/%s" % topic

def collection_subscription_url(publication):
    return ME_URL + "/subscriptions/collection/%s" % publication

def activity_url():
    return ME_URL + "/activity"

def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text  # or whatever

def fix_medium_json_response(data):
    return remove_prefix(data, "])}while(1);</x>")

def get_activity(access_token):
    headers = {
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
        "Authorization": "Bearer %s" % access_token,
        "User-Agent":str(ua.random),
        "x-xsrf-token": access_token,
        "cookie": COOKIE,
        "content-type": "application/json"
    }
    url = activity_url()
    r = requests.get(url, headers = headers)
    data = json.loads(fix_medium_json_response(r.text))
    return data

def subscribe(access_token, topic=None, publication=None):
    url = None
    if topic is None:
        topic = publication.replace(" ", "-")
        url = collection_subscription_url(topic)
    elif publication is None:
        topic = topic.replace(" ", "-")
        url = topic_subscription_url(topic)
    else:
        print("Both topic and publication can't both be none")
        return
    print(url)

    headers = {
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
        "Authorization": "Bearer %s" % access_token,
        "User-Agent":str(ua.random),
        "x-xsrf-token": access_token,
        "cookie": COOKIE
    }
    r = requests.put(url, headers = headers)
    print(r.text)

# Get articles from home page
def get_home_articles(access_token):
    headers = {
        "Accept": "application/json",
        "Accept-Charset": "utf-8",
        "Authorization": "Bearer %s" % access_token,
        "User-Agent":str(ua.random),
        "x-xsrf-token": access_token,
        "cookie": COOKIE
    }
    try:
        r = requests.get(PRIVATE_API_URL + "/home-feed", headers = headers)
        data = json.loads(fix_medium_json_response(r.text))
        stream_items = data["payload"]["streamItems"]
        for post in stream_items:
            # print(post)
            # print("Continue (y/n)")
            # should_continue = sys.stdin.readline().strip()
            # if should_continue == "n":
            #     continue
            item_type = post["itemType"]
            if item_type == "extremePostPreview":
                post_preview = post["extremePostPreview"]
                post_id = post_preview["postId"]
                print(post_url(post_id))
            elif item_type == "extremeAdaptiveSection":
                if "items" in post:
                    items = post["items"]
                    for item in items:
                        item_post = item["post"]
                        post_id = item_post["postId"]
                        print("----extremeAdaptiveSection!!!!")
                        print(post_url(post_id))
    except requests.exceptions.ConnectionError:
        print("Connection refused")
    
    


if __name__ == '__main__':
    do_auth = True

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
        # user = client.get_current_user()
        # print(user)

        # Get publications
        # publications = client._request("GET", "/v1/users/" + user["id"] + "/publications")
        # print(publications)

        # get_home_articles(client.access_token)
        
        # subscribe(client.access_token, publication="greylock perspectives")

        print(get_activity(client.access_token))


# # Create a draft post.
# post = client.create_post(user_id=user["id"], title="Title", content="<h2>Title</h2><p>Content</p>",
#                           content_format="html", publish_status="draft")

# # When your access token expires, use the refresh token to get a new one.
# client.exchange_refresh_token(auth["refresh_token"])

# # Confirm everything went ok. post["url"] has the location of the created post.
# print("My new post!", post["url"])