class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

people_are_strange = Song(["People are strange when you're a stranger",
                           "Faces look ugly when you're alone",
                           "Women seem wicked when you're unwanted",
                           "Streets are uneven when you're down"])

the_crystal_ship = Song(["The crystal ship is being filled",
                         "A thousand girls, a thousand thrills",
                         "A million ways to spend your time",
                         "When we get back, I'll drop a line"])

people_are_strange.sing_me_a_song()

the_crystal_ship.sing_me_a_song()
