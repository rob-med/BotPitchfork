import tweepy
import requests
import datetime
params = {
	'api_key': "XXXX",
	'url': "https://pitchfork.com/best/",
	'model_id': "XXXX"
}

response = requests.get('https://api.dashblock.io/model/v1', params=params)

tracks = response.json()
print(tracks)
tracks = tracks['entities']


# Authenticate to Twitter
auth = tweepy.OAuthHandler("XXXX", "XXXX")
auth.set_access_token("XXXX", "XXXX")

# Create API object
api = tweepy.API(auth)
last_tweeted = api.user_timeline(count=1)[0].created_at

for t in tracks:
	#for i in range(3):
		ts = t['date'].strip()
		print(ts)
		post = "ago" in ts
		if not post:
			ts = datetime.datetime.strptime(ts, '%B %d %Y')
			print(ts, last_tweeted)
			post = last_tweeted < ts

		if post:	
			try:
				# Create a tweet
				api.update_status(f"{t['title']} by {t['artist']} is {t['tag'].upper()} on @Pitchfork. {t['title:link']} #{t['artist'].replace(' ','')} #pitchfork #bestnewmusic")
			except tweepy.TweepError:
				print('No update.')
