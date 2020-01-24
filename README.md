# BotPitchfork, a Pitchfork Twitter bot

This repo contains the code running the [BotPitchfork](https://twitter.com/BotPitchfork) Twitter bot, which tweets Pitchfork's best new music - tracks, albums and reissues - as soon as it's announced. 
The bot is built using [Dashblock](https://dashblock.com) and [Tweepy](http://tweepy.org).
Everything is hosted on Heroku, with a Flask app.

## Description

A detailed description of the project can be found [on Medium]().


## Hosting 

The template used to host the Flask app on Heroku comes from:
https://github.com/yefim/flask-heroku-sample.

There, you will also find instructions on its deployment.

## Automated Tweeting
To enable constant monitoring and automated tweeting you need to create a cron job in Heroku, and this can be done using the [Heroku Scheduler](https://addons-sso.heroku.com/apps/d1734328-bd3f-484a-ac91-2e1aa2627c80/addons/1370e47f-2612-4cae-a639-19fc0527d03c) add on, connected to the **post.py** script.


