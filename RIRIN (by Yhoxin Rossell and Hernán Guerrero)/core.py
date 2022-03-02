import quotes_lib

def get_random_quote():
  msg = ''

  try:
    quote, author = quotes_lib.get_random_quote()
    msg = f'{quote}\n  by {author}'

  except Exception as e:
    print(e)
    msg = "Ther's and connection error, try again."

  return msg