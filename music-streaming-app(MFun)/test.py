class MusicLibrary:
    def __init__(self):
        self.songs = []
        self.unique_songs = set(self.songs)
    def add_song(self, song):
        self.songs.append(song)
        self.unique_songs = set(self.songs)
    
    def print_song(self):
        for i in self.unique_songs:
            print(i)
        

library = MusicLibrary()
song1 = "song1"
song2 = "song2"
song3 = "song3"
song4 = "song4"

library.add_song(song1)
library.add_song(song2)
library.add_song(song3)
library.add_song(song4)

library.print_song()