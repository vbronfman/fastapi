import random
import time
from datetime import date
from itertools import groupby

class MusicPlayer:
    last_song = str()

    def __init__(self, playlist: list[str] ):
        self.playlist = playlist

    def is_uniq(self) -> bool:
        for i,song in enumerate(self.playlist):
            if song[i] == song[i-1]:
                print (" DEBUG Not uniq")
                return False
        
        return True    

    def is_uniq_with_groupby(self):
        
        if any([ k for k,i in groupby(self.playlist) if len(list(i)) > 1 ]):
            return False
        else: 
            return True


    def play(self) -> None:
        while True:
            print (f"Playlist: {self.playlist}")
#            while not self.is_uniq():
            while not self.is_uniq_with_groupby():
                print(f"DEBUG : not uniq : {self.playlist}")
                random.shuffle(self.playlist)

            for i in self.playlist:
                print (f"{i}")
                time.sleep(1)
            
            random.shuffle(self.playlist)



playlist = ["Gods Plan", "A LA SALA", "Hate That I Love You", "Texas Sun", "Gods Plan"]

player = MusicPlayer(playlist)
#player.play()

playlists = {
"20240131": ["Gods Plan", "A LA SALA", "Hate That I Love You", "Texas Sun", "Gods Plan"],
"20240130": ["Another Love", "THANK GOD", "THANK GOD", "Gods Plan", "fukumean"],
"20240115": ["Tobacco Sunburst", "Tobacco Sunburst", "Sofia", "Bloom Later", "Gods Plan"],
"20230201": ["Gods Plan", "Nonstop", "In My Feelings", "In My Feelings", "March 14"],
"20240321": ["Gods Plan", "Nonstop", "In My Feelings", "In My Feelings", "March 14"]
}

# - get_closest_playlist(): get the closest (by date) playlist.

today = date.today() 
print ("{}".format(today := int(today.strftime("%Y%m%d"))))
print(f"{today=}",type(today))




