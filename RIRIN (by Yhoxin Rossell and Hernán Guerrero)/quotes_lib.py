from urllib import request
import json

def get_random_quote():
  """Function that return a tuple of
  quote and author strings from zenquotes API.
  """
  quote, author = '', ''

  # make requires
  req = request.Request(url='https://zenquotes.io/api/random')

  # send request
  print('waiting for response...')
  with request.urlopen(req, timeout=10) as res:
    print('conection open!')
    # wait until the data resived is fully readed,
    # and decode with utf-8.
    raw_string = res.read().decode('utf-8')

    # convert raw_string json into a dictionary.
    data = json.loads(raw_string)

    # the data resived is an array with only 1
    # element of structure:
    #  {
    #     "q": "the string quote...",
    #     "a": "the author."
    #  }
    quote = data[0]['q']
    author = data[0]['a']
    
  return quote, author

def get_50_quotes():
  """Function that return a tuple of
  quote and author strings from zenquotes API.
    [
      {
        "q": "the quote...",
        "a": "the author."
      }
    ]
  """
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