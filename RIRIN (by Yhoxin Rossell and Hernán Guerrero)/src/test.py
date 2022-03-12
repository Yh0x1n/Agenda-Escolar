from pathlib import Path
import unittest

import core

class Test(unittest.TestCase):
  def test_one(self):
    # to-do: specify a temporary data folder
    dir_path = core.ensure_data_folder()

    print(f'The data folder:{dir_path}')
    self.assertTrue(dir_path.exists())

    # Get Data base...
    db = core.DataBase(str(dir_path))
    self.assertTrue(Path(db.path).exists())

    # Save quote...
    q = {
      "author": 'author 1',
      "content": 'text',
      "year": 100
    } # the quote
    res = db.quotes.save(q)

    # Retrive quote...
    res = db.quotes.get({'author': q['author']})

    # Check if saved...
    self.assertEqual(res[0].content, q['content'])

    # Delete all quotes...
    res = db.quotes.delete()
    self.assertEqual(res['count'], 1)

    res = db.quotes.get()
    self.assertEqual(len(res), 0)

if __name__ == '__main__':
  unittest.main()