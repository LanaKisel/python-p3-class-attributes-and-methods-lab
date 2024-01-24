class Song:
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.add_to_genre_count(genre)
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def add_to_artists(self, artist):
        self.add_to_artist_count(artist)
        if artist not in self.artists:
            self.artists.append(artist)
    @classmethod
    def add_to_genre_count(self, genre):
        if genre not in self.genres:
            self.genre_count[genre] = 0
        self.genre_count[genre] += 1
    @classmethod
    def add_to_artist_count(self, artist):
        if artist not in self.artists:
            self.artist_count[artist] = 0
        self.artist_count[artist] += 1    
