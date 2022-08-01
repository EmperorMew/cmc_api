# use coinmarketcap api

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'API_KEY'
}

parameters = {
    'start': '1',
    'limit': '100',
}

session = Session()
session.headers.update(headers)

address_list = []
tag = "dao"

# function returns the 0x address associated with specified tag:

def address_exists(data, addy_list, selected_tag):

    for entry in data['data']:
        platform = selected_tag in entry['tags'] and entry['platform']

        if bool(platform) and platform['token_address'] != "":
            token_address = platform['token_address']

            if token_address.startswith("0x"):
                addy_list.append(token_address)

                continue

# function executes address_exists function and returns the results in a list:

def get_tag_address():

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        address_exists(data, address_list, tag)

        return address_list

    except (ConnectionError, Timeout, TooManyRedirects) as e:

        print('error:', e)

print(get_tag_address())
