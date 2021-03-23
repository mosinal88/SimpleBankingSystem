class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        print('"{}" by {} ({}) hangs in the {}.'.format(title, artist, year, Painting.museum))


Painting(input(), input(), input())
