from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import urllib


def url_validator(url):
    try:
        code = urllib.urlopen(url).getcode()
        if code == 200:
            return True
    except:
        return False


def test_url(message, url):
    if url_validator(url[1:len(url)-1]):
        message.reply('VALID URL')
    else:
        message.reply('NOT VALID URL')
