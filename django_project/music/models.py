from django.db import models

#say we have an album named Red with pk=1
#we link a song to an album via foreignkey 
#on delete...part means when we delete our album delete all songs
class Album(models.Model): #basically fixing datatype
    artist=models.CharField(max_length=250)   
    album_title=models.CharField(max_length=500)
    genre=models.CharField(max_length=100)
    album_logo=models.CharField(max_length=1000)
#this is the string representation of our class

    def __str__(self):
        return self.artist+' - '+self.album_title

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=10)
    song_title=models.CharField(max_length=250)
