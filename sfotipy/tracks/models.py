from django.db import models

from artists.models import Artist
from albums.models import Album

class Track(models.Model):
	title = models.CharField(max_length=255)
	order = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='tracks')
	artist = models.ForeignKeyField(Artist)
	album = models.ForeignKeyField(Album)

	def __unicode__(self):
		return self.title