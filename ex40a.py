class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

passenger = ["\nWell you only need the light when it's burning low\n",
"\nOnly miss the sun when it starts to snow\n",
"\nOnly know you love her when you let her go\n",
"\nOnly know you've been high when you're feeling low\n",
"\nOnly hate the road when you're missing home\n",
"\nOnly know you love her when you let her go\n",
"\nAnd you let her go\n"]

Let_Her_Go = Song(passenger)

Let_Her_Go.sing_me_a_song()
