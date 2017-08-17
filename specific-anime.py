import subprocess
import json
import uuid
from pymongo import MongoClient

anime_title = "Tokyo Ghoul"
anime_url = "https://youtu.be/eNGhKIcHVQc"
anime_img_url = "http://agarioskins.com/submitted/useruploads/tokyo%20ghoul%20png%201.png"
alert_img = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/OOjs_UI_icon_alert_destructive.svg/2000px-OOjs_UI_icon_alert_destructive.svg.png"
anime_description = "A 12 episode psychological thriller (but not quite horror...can anime ever really be horror?) with one of the best opening songs."
family_friendly = "NO"
where_to_watch = "Circulating Apple for a limited time only! Streaming on Funimation and Hulu."
for_whom = "People who can stomach some amount of 2D animated violence and psychological thrillers."

test_url = "https://ichat.apple.com/v2/room/6715/notification?auth_token=2Inlmv47cujCGjKOg5C1JnAFrQbwlh7Oc3OGfN2i"
production_url = "https://ichat.apple.com/v2/room/6394/notification?auth_token=8zqDOBp2z3q4sSceW5oHEt9w24JkXiaq5lQVzNOK"
mongodb_uri = "mongodb://heroku_sjwpcpmp:bot3lu7crprs0qm1mhdsv40pv7@ds121091.mlab.com:21091/heroku_sjwpcpmp"
mongodb_client = "heroku_sjwpcpmp"

template = { "notify":True,"message":"foo","card":{
  "style": "application",
  "url": anime_url,
  "format": "medium",
  "id": "db797a68-0aff-4ae8-83fc-2e72dbb1a707",
  "title": anime_title,
  "description": anime_description,
  "icon": {
    "url": anime_img_url
  },
  "attributes": [
    {
      "label": "For",
      "value": {
        "label": for_whom
      }
    },
    {
      "label": "Where to watch?",
      "value" : {
        "label":where_to_watch
      }
    },
    {
      "label": "Family friendly?",
      "value": {
        "icon": {
          "url": alert_img
        },
        "label": family_friendly,
        "style": "lozenge-complete"
      }
    }
  ]
  }
}



def set_template(anime_title, anime_url, anime_img_url, anime_description, for_whom, where_to_watch, family_friendly):
  template = { "notify":True,"message":"foo","card":{
  "style": "application",
  "url": anime_url,
  "format": "medium",
  "id": "db797a68-0aff-4ae8-83fc-2e72dbb1a707",
  "title": anime_title,
  "description": anime_description,
  "icon": {
    "url": anime_img_url
  },
  "attributes": [
    {
      "label": "For",
      "value": {
        "label": for_whom
      }
    },
    {
      "label": "Where to watch?",
      "value" : {
        "label":where_to_watch
      }
    },
    {
      "label": "Family friendly?",
      "value": {
        "icon": {
          "url": alert_img
        },
        "label": family_friendly,
        "style": "lozenge-complete"
      }
    }
  ]
  }
  }
  return template


def get_db():
    client = MongoClient(mongodb_uri)
    db = client[mongodb_client]
    return db

def get_new_info():
  database = get_db()
  news = database.applenews.find({})
  for new in news:
    if "used" not in new:
      print "Not used yet"
      # post to hip chat with the data!
      anime_title = new["anime_title"]
      anime_description = new["anime_description"]
      anime_url = new["anime_url"]
      anime_img_url = new["anime_img_url"]
      family_friendly = new["family_friendly"]
      for_whom = new["for_whom"]
      where_to_watch = new["where_to_watch"]
      template = set_template(anime_title, anime_url, anime_img_url, anime_description, for_whom, where_to_watch, family_friendly)
      main(template)
      database.applenews.update({"_id": new["_id"]}, {"$set": {"used": True}})
      return
    else:
      print "Used"
      print new

def insert_anime():
  database = get_db()
  database.applenews.insert_one({"anime_title":"Death Note", "anime_url":"https://www.hulu.com/death-note", "anime_description":"An anime classic about a guy who finds a notebook with the ability to kill anyone whose name is written in it.", "family_friendly":"Just not for young children", "where_to_watch":"Youtube, Hulu, Netflix", "for_whom":"I recommend this show to just about everyone. Again, classic"})


def main(template):
  command = "curl -d '" + json.dumps(template) + "' -H 'Content-Type: application/json' " + test_url
  p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
  out, err = p.communicate()

if __name__ == '__main__':
  #insert_anime()
  get_new_info()
  #smain()
  print "done"