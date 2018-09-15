import os
import pathlib
from pathlib import Path
from collections import namedtuple
import random
import quotes_lib

import sqlite3

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

def ensure_data_folder(folder_path=''):
  APPDATA = os.getenv('APPDATA')
  dir_path = pathlib.Path(f'{APPDATA}/ririn')

  if not dir_path.exists():
    dir_path.mkdir()

  return dir_path

Quote = namedtuple('Quote', 'author content year popularity', defaults=(None,) * 4)

class QuotesDB:
  def __init__(self, connection):
    self.con = connection
    self.name = 'quotes'
    self.ensure_table()

  def exists_table(self):
    with self.con as c:
      res = c.execute('select name from sqlite_master where type="table" and name=(?)', (self.name,)).fetchall()
    return len(res) > 0

  def ensure_table(self):
    with self.con as c:
      if not self.exists_table():
        c.execute(f"""create table {self.name}
        (author text, content text, year integer, popularity integer)""")  

  def save(self, quote):
    q = Quote(**quote)

    with self.con as c:
      res = c.execute("insert into quotes values (?, ?, ?, ?)", q).fetchall()

    return res

  def get(self, filters={}, order_by=[]):
    quotes = []
    query = "select * from quotes "

    if filters:
      query += "where "

      for k in filters.keys():
        query += f'{k}=:{k} '

    if len(order_by) > 0:
      query += "order by "
      for o in order_by:
        query += o + " "
      
    with self.con as c:
      quotes = c.execute(query, filters).fetchall()
      quotes = [ Quote(*q) for q in quotes ]
    
    return quotes  

  def delete(self, filters={}):
    query = 'delete from quotes'

    if filters:
      query += 'where '
      for k in filters.keys():
        query += f'{k}=:{k} '

    with self.con as c:
      cursor = c.execute(query, filters)()
      res = {
        'count': cursor.rowcount
      }

    return res

class DataBase:
  def __init__(self, dir_path):

    self.path = f'{dir_path}/data.db'
    self.connection = sqlite3.connect(self.path)
    self.quotes = QuotesDB(self.connection)