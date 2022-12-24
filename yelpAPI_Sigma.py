import requests
API_KEY = 'kuUyvVGaxXKo9mso5tInqtJ6U2beSUpj82lipxnwjbDEuLK31zulgEREKinpGAJNcwqVNbAVd_9Ka82qdS_QsanYSiEJW0SN81zKNFnIxBmaVv2SzTLLZde1w91YY3Yx'
# Header is metadata to authenticate yourself ..to do this, create a dictionary
HEADERS = {"Authorization": "bearer %s" %API_KEY}

# 1. BUSINESS SEARCH ENDPOINT
print('Business Search Endpoint\n')
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
PARAMETERS = {'term':'coffee',
              'limit': 50,
              'radius': 10000,
# NOTE: it'll return businesses 200-250 cuz of this offset
# (simply remove this for first 50 results)
              'offset': 200,
              'location': 'San Diego'}
# Make request to the API
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
# Convert json string to dictionary object
business_data = response.json()
# We can print a SHITLOAD of info w this:
##print(business_data)

# OR WRITE IT TO A FILE! FUCK YEA I FIGURED THIS OUT KINDA MYSELF!!!
##with open('biz.txt', 'w') as f:
##    f.write(str(business_data))

# ..or select the dictionary key we want
for biz in business_data['businesses']:
    print(biz['name'])


# 2. BUSINESS MATCH ENDPOINT
##print('Business Match Endpoint\n')
##ENDPOINT = 'https://api.yelp.com/v3/businesses/matches'
##PARAMETERS = {'name': 'Peets Coffee & Tea',
##              'address1': '7845 Highland Village Pl',
##              'city': 'San Diego',
##              'state': 'CA',
##              'country': 'US'}
##response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
##business_data = response.json()
##for biz in business_data['businesses']:
##    print(biz)


# 3. BUSINESS PHONE SEARCH ENDPOINT
##print('\nBusiness Phone Search Endpoint\n')
##ENDPOINT = 'https://api.yelp.com/v3/businesses/search/phone'
##PARAMETERS = {'phone': '+18584340001'}
##response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
##business_data = response.json()
##for biz in business_data['businesses']:
##    print(biz)


# 4. PASS THRU BUSINESS ID FOR MORE DETAILED INFO
##print('\nDetailed Info Using Business ID\n')
##business_id = '4AErMBEoNzbk7Q8g45kKaQ'
##ENDPOINT = 'https://api.yelp.com/v3/businesses/{}'.format(business_id)
### note we don't use params here w .get method
##response = requests.get(url = ENDPOINT, headers = HEADERS)
##business_data = response.json()
##for cats in business_data['categories']:
##    print(cats)

# 5. REVIEWS ENDPOINT
##print('\nReviews Endpoint - using Business ID\n')
##business_id = '4AErMBEoNzbk7Q8g45kKaQ'
##ENDPOINT = 'https://api.yelp.com/v3/businesses/{}/reviews'.format(business_id)
##response = requests.get(url = ENDPOINT, headers = HEADERS)
##business_data = response.json()
##print(business_data)
