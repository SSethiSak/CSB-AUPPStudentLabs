"""
You are part of a team developing a new music streaming app called "MFun." Your task is to design the core functionality that manages the user's music library and playlist creation. Consider the following requirements:

Music library:
Needs to store a collection of songs and their associated metadata (title, artist, album, genre, length).
Must efficiently retrieve songs by various criteria (artist, album, genre, title).
Must prevent duplicate song entries.

Playlists:
Users can create unlimited playlists.
Each playlist can contain any number of songs, but a song cannot be added multiple times to the same playlist.
Songs can be added, removed, or reordered within playlists.
The app should display songs in the order they were added to the playlist.

Which data structure model(s) would you choose to implement the music library and playlist features? Explain your choices, considering the characteristics of each data structure and the specific requirements of the application.

Data structures to consider:
       Tuples, Sets, Lists, Dictionaries, Trees, Graphs, Stacks, Queues
"""
# Prototype code, you can follow different implementation process
from collections import deque 
from typing import Any


class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length
        
    def __str__(self):
        return f"{self.title}, {self.artist}, {self.album}, {self.genre}, {self.length}"

class MusicLibrary:
    def __init__(self):
        self.songs = []
        self.unique_songs = set(self.songs)
    def add_song(self, song):
        self.songs.append(song)
        self.unique_songs.add(song)
        
    def get_songs_by_artist(self, artist):
        for i in self.unique_songs:
            if i.artist == artist:
                return i
            
    def get_songs_by_album(self, album):
        for i in self.unique_songs:
            if i.album == album:
                return i
            
    def get_songs_by_genre(self, genre):
        for i in self.unique_songs:
            if i.genre == genre:
                return i
            
    def get_songs_by_title(self, title):
        for i in self.unique_songs:
            if i.title == title:
                return i
    
    def show_all_songs(self):
        for i in self.unique_songs:
            print(i)
            
            
class Playlist:
    def __init__(self, name):
        self.playlist = []
        self.unique_playlist = set()
        self.playlist_name = name
        
    def add_song(self, song):
        self.playlist.append(song)
        self.unique_playlist.add(song)
        
    def remove_song(self, song):
        self.playlist.remove(song)
        for i in range(len(self.playlist)):
            if self.playlist[i] == song:
                self.playlist.pop(i)
        
    def reorder_songs(self, new_order):
        if new_order == "oldest":
            new_list = list(self.playlist)
            new_list.reverse()
            self.playlist = new_list
        else:
            pass
            
    def display_playlist(self):
        count = 0
        print(f"Playlist: {self.playlist_name}")
        for i in self.playlist:
            count += 1
            print(f"#{count}. {i.title} - {i.artist}")
    
    
# Main Requirement:
# Create song example
# Create a music library
# Add songs to the music library
# Get songs by artist
# Create playlists
# Add songs to playlists
# Display playlists
# Searching for songs by artist

# Sample Output:
# Playlist: My Playlist 1
# 1. Song 1 - Artist 1
# 2. Song 2 - Artist 2

# Songs by Artist 1:
# Song 1 - Album 1


song_1 = Song("song title 1", "artist1", None, "Rock", 214)
song_2 = Song("song title 2", "artist2", "album-45", "pop", 322)
song_3 = Song("song title 3", "artist3", "album-25", "cheerful", 322)
song_4 = Song("song title 4", "artist2", "album-64", "jazz", 322)

Library = MusicLibrary()
Library.add_song(song_1)
Library.add_song(song_2)
Library.add_song(song_1)
Library.add_song(song_3)
Library.add_song(song_4)

Library.show_all_songs()

My_Playlist = Playlist("Sak's Playlist")

My_Playlist.add_song(song_1)
My_Playlist.add_song(song_2)
My_Playlist.add_song(song_3)
My_Playlist.remove_song(song_1)
My_Playlist.add_song(song_4)

My_Playlist.display_playlist()
My_Playlist.reorder_songs("oldest")
My_Playlist.display_playlist()