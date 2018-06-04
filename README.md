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