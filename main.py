import argparse
from decouple import config
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

parser = argparse.ArgumentParser(description='get symbol to search')
parser.add_argument('-sym', '--symbol', type=str, help='symbol to get the ID.')
args = parser.parse_args()

urlMetadata = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

paramsMetadata = {
  'symbol': f'{str(args.symbol)}',
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': config('API_KEY'),
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(urlMetadata, params=paramsMetadata)
  data = json.loads(response.text)
  print(data['data'][f'{str(args.symbol)}']['id'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)