# Yelp API Categories Endpoint
import requests
# Since we're parsing json strings
import json
API_KEY = 'kuUyvVGaxXKo9mso5tInqtJ6U2beSUpj82lipxnwjbDEuLK31zulgEREKinpGAJNcwqVNbAVd_9Ka82qdS_QsanYSiEJW0SN81zKNFnIxBmaVv2SzTLLZde1w91YY3Yx'
HEADERS = {"Authorization": "bearer %s" %API_KEY}
##endpoint = 'https://api.yelp.com/v3/categories'
##response = requests.get(url = endpoint, headers = HEADERS)
##taint = response.json()
# Calling json library, dumps() method, which takes
# a string object and indent as arg's
# ..which returns a RETARDED amount of data (20k lines)
##print(json.dumps(taint, indent = 3))

# SO.. how to loop thru this object? We first notice
# a massive list called categories w individual dictionaries
# ..so loop thru response ('taint'.. lol) to get EVERY category
# (looping thru dicitonaries within a list)
##for item in taint['categories']:
##    print(item['title'])

# Can also change endpoint to specific category
# (must use alias, not name)
##endpoint = 'https://api.yelp.com/v3/categories/gokarts'
##response = requests.get(url = endpoint, headers = HEADERS)
##taint = response.json()
##print(json.dumps(taint, indent = 3))


# Yelp API Transaction Endpoint
# (apparently delivery is the only transaction type.. don't get this)
##endpoint = 'https://api.yelp.com/v3/transactions/delivery/search'
##parameters = {'location':'Chicago'}
##response = requests.get(url = endpoint, headers = HEADERS, params = parameters)
##taint = response.json()

# Print the whole mess..
##print(json.dumps(taint, indent = 3))

# OR.. print just the name key, for example
##for item in taint['businesses']:
##    print(item['name'])
##    print(item['id'])

# Yelp API Autocomplete Endpoint
# (think of it kinda like a search engine query)
endpoint = 'https://api.yelp.com/v3/autocomplete'
parameters = {'text':'strippers',
              'latitude':36.184599,
              'longitude':-115.23199}
response = requests.get(url = endpoint, headers = HEADERS, params = parameters)
scrotum = response.json()
print(json.dumps(scrotum, indent = 3))
