import random
import quotes_lib

def get_random_quote():
  msg = ''
  try:
    quote, author = quotes_lib.get_random_quote()
    msg = f'"{quote}"\n\nby {author}'
  except Exception as e:
    print(e)
    msg = "There's and connection error, try again."

  return msg

def get_motivation_phrase():
  phrases = ["Keep it up! You're almost there!",
    "You are great, you are beautiful,\nyou are everything that's fine.",
    "Love yourself.",
    "You're an angel.",
    "You make everyone blind\nbecause you're shining bright.",
    "We dream with the day you'll be turning\ninto a succesful person.",
    "Look at the sky before you go to sleep...\nYou see? We're under the same sky as you,\neven though the time is different.",
    "You're never alone.",
    "My shoulder is yours if you need to cry.\nJust let it out. It's okay.~",
    "Be yourself, speak yourself",
    "If you can imagine it, you can make it true.\nThe only limit is your mind.",
    "Don't let anyone make you believe\nthat you can't do something."]
    
  msg = random.choice(phrases)
  return msg