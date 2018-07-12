class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

right_there = Song(["Happy birthday to you",
                    "I don't want to get sued",
		    "So I'll stop right there"])

pockets_of_shells = Song(["They rally around tha family",
                          "With pockets full of shells"])

right_there.sing_me_a_song()

pockets_of_shells.sing_me_a_song()
