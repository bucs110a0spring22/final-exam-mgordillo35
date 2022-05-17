import requests

class Amiibo:
  def __init__(self, name):
    self.url = f'https://amiiboapi.com//api/amiibo/?{name}'
    
  def get(self):
    r = requests.get(self.url)
    response = r.json()

    type = response['amiibo']
    type2 = type[1]
    
    print(f'This is its type: {type2}')

    

    
    

    

    
    
    