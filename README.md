# Simplify life scripts

## animeStreamingInfo.py
Get anime streaming information

## anonMail.py
Mass spam anonymous emails

## beSocial.py
Mass imessage people

## createFlask.py
Just create some files and folders that I always use for flask apps

## new_anime_rec.py
Recommend anime by season. See my [anime-server](https://github.com/Lucytheanimefan/anime-server) for the better recommender. 

## newDeadFishProj.py
Just create some files and folders that I always use for (deadfisheyed.herokuapp.com)

## specific_anime.py
Inserting anime into my db to make hipchat extension for anime notifications to work group. 

## sendMessage.applescript
Send an iMessage with a text message and/or a file attachment to a person with phone number.

Example:

`osascript sendMessage.applescript 9848888888 "test image and text" "/Users/billyu/Desktop/violet/violet.PNG"`

## com.billyu.botherlucy.plist
Bother Lucy daily with the Violet Evergarden image.

setup:

1. `sudo cp com.billyu.botherlucy.plist /Library/LaunchDaemons/`
2. Replace the placeholder phone number with the real one.
3. Edit the daily message && correct the script and image paths if necessary.
4. `sudo launchctl load /Library/LaunchDaemons/com.billyu.botherlucy.plist`
5. Start bothering Lucy on a daily basis.

## newNpm.sh

Initializes an npm project with configured settings.

usage:

1. cd into this project's directory
2. sh ./newNpm.sh {absolute directory of the new project}

## mediumPublications.py
Alternative interface to the limited existing medium API. Can pull custom Medium recommended articles from home feed. 

### Setup
1. Created a .env file in the same directory as the script. In the file, set your COOKIE variable, which you can get from the dev tools in chrome in the Network tab. Also set MEDIUM_CLIENT_ID and MEDIUM_CLIENT_SECRET. 
2. Make sure you have the following python modules installed: dotenv, medium.
