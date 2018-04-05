 #!/usr/bin/env python3
import unittest
import sqlite3
import os
import db

class Testdb(unittest.TestCase):

    def setUp(self):
        conn = sqlite3.connect('stories.db')
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS stories (name TEXT, content TEXT)")
        conn.commit()
        conn.commit()
        file = open('new.txt', 'w')
        file.write('story time')
        file.close()

    def tearDown(self):
        conn = sqlite3.connect('stories.db')
        c = conn.cursor()
        c.executescript('DROP TABLE IF EXISTS stories;')
        conn.commit()
        path = '/home/pi/AIY-voice-kit-python/src/examples/voice/StoryVoice'
        for file in os.listdir(path):
            if file.endswith(".txt"):
                os.remove(file)

    def test_setS(self):
        result = db.setS()
        self.assertEqual(result, 1)

    def test_how_many(self):
        result = db.how_many()
        self.assertEqual(result, 0)

    def test_save_and_retrieve_story(self):
        db.save_story('new.txt')
        db.saved_story('one')
        expected = ('story1.txt')
        self.assertTrue(expected)
        result = db.how_many()
        self.assertEqual(result, 1)
        s = db.setS()
        self.assertEqual(s, 2)

    def test_clear(self):
        db.save_story('new.txt')
        db.clear()
        result = db.how_many()
        self.assertEqual(result, 0)
        s = db.setS()
        self.assertEqual(s, 1)

if __name__ == '__main__':
    unittest.main()
