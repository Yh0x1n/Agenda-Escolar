from urllib import request
import json

def get_random_quote():
  quote, author = '', ''

  # make requires
  req = request.Request(url='https://zenquotes.io/api/random')

  # send request
  print('waiting for response...')
  with request.urlopen(req, timeout=10) as res:
    print('conection open!')
    # get content    
    raw_data = res.read().decode('utf-8')
    data = json.loads(raw_data)
    quote = data[0]['q']
    author = data[0]['a']
    
  return quote, author

def get_50_quotes():
  quotes = []

  req = request.Request(url='https://zenquotes.io/api/quotes')
  with request.urlopen(req) as res:
    raw_data = res.read().decode('utf-8')
    quotes = json.loads(raw_data)

  return quotes

def main():
  quote, author = get_random_quote()
  print(f'"{quote}" by {author}')

if __name__ == "__main__":
  main()