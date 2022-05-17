import requests

class Pokemon:
  def __init__(self, name):
      self.url = f'https://pokeapi.co/api/v2/pokemon/{name}/'
    
  def get(self, name):
      r = requests.get(self.url)
      response = r.json()
  
      abilities1 = response['abilities']
    
      print(f'These are {name}\'s stats: {abilities1}')

      #gaga responsibilities

      

      

    