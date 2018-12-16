import constants
import oauth2
import urllib.parse as urlparse

#create a consumer, only used to identify the app
consumer = oauth2.Consumer(constants.CONSUMER_KEY, constants.CONSUMER_SECRET)

#create a client to make requests
client = oauth2.Client(consumer)

response, content = client.request(constants.REQUEST_TOKEN_URL, 'POST')

if response.status != 200:
  print('An error occurred getting the request token from Twitter')

request_token = dict(urlparse.parse_qsl(content))

