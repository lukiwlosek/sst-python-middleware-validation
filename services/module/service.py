import requests


def make_external_request():
  print('here')
  r = requests.get('https://njjpcmn4vd.execute-api.eu-west-1.amazonaws.com/test')
  print(r)