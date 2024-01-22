#This unittest file tests the core functionality of the MFun class. You can expand it by adding more test methods for other methods in the class.

import unittest

class TestMFunMethods(unittest.TestCase):
    def setUp(self):
        self.musicLibrary = MusicLibrary()
        self.playList = Playlist()

    def test_add_song(self):
        self.assertTrue(self.musicLibrary.add_song("Songa", "Artista", "Albuma", "Genrea", "3:00"))
        self.assertFalse(self.musicLibrary.add_song("Songb", "Artistb", "Albumb", "Genreb", "3:30")) 

    def test_display_playlist(self):
        self.playList.display_playlist()

if __name__ == '__main__':
    unittest.main()
