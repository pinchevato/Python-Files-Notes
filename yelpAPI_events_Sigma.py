# Events API for Yelp, very similar to Businesses API
import requests
API_KEY = 'kuUyvVGaxXKo9mso5tInqtJ6U2beSUpj82lipxnwjbDEuLK31zulgEREKinpGAJNcwqVNbAVd_9Ka82qdS_QsanYSiEJW0SN81zKNFnIxBmaVv2SzTLLZde1w91YY3Yx'
HEADERS = {"Authorization": "bearer %s" %API_KEY}

# EVENT LOOKUP ENDPOINT
event_id = 'oakland-saucy-oakland-restaurant-pop-up'
ENDPOINT = 'https://api.yelp.com/v3/events/{}'.format(event_id)

#No parameters in this example (locale is optional)
##response = requests.get(url = ENDPOINT, headers = HEADERS)
##event_data = response.json()

#Print whole fkn thing
##print(event_data)
# ..or just one key in the dictionary
##print(event_data['description'])


# USEFUL!! DICTIONARY BUILT IN METHODS:
# see all keys
##print(event_data.keys())
# see all values
##print(event_data.values())
# same as print(event_data) but w slightly different syntax.. don't really fuckin get it whatev
##print(event_data.items())


# EVENT SEARCH ENDPOINT
ENDPOINT = 'https://api.yelp.com/v3/events'
PARAMS = {'location':'New York City',
# just look at 5 events, default is only 3
          'limit': 5}
response = requests.get(url = ENDPOINT, params = PARAMS, headers = HEADERS)
ev_data = response.json()

for ev in ev_data['events']:
# We could look in documentation or just do this:
##    print(ev.keys())
# ..and for example, use the 'is_free' key:
    print(ev['location'])


# FEATURED EVENTS ENDPOINT (seems like featured evens are rare)
print('\n\n')
ENDPOINT = 'https://api.yelp.com/v3/events/featured'
response = requests.get(url = ENDPOINT, params = PARAMS, headers = HEADERS)
ev_data = response.json()
##print(ev_data)
