from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import urllib

import database


def url_validator(url):
    try:
        code = urllib.urlopen(url).getcode()
        if code == 200:
            return True
    except:
        return False


@respond_to('[Tt]est (\<[\w\d\s\:\/\.\-\_]*[\>\|])')
def test_url(message, url):
    if url_validator(url[1:len(url)-1]):
        message.reply('VALID URL')
    else:
        message.reply('NOT VALID URL')


@respond_to('[[Dd]atabase test')
def test_db(message):
    if database.check_db():
        message.reply('I can see the database.')
    else:
        message.reply('I can\'t see the database.')
        message.reply('To create one write `database create`')


@respond_to('[Dd]atabase create')
def create_db(message):
    if database.check_db():
        message.reply('Database already exists.')
    else:
        message.reply(database.create_db())

