from django.contrib import admin

from .models import Artist

from tracks.models import Track
from albums.models import Album

class TrackInLine(admin.StackedInline):
	model = Track
	extra = 1

class AlbumInLine(admin.StackedInline):
	model = Album
	extra = 0

class ArtistAdmin(admin.ModelAdmin):
	search_fields = ('first_name', 'last_name')
	#filter_horizontal = ('favorite_songs', )
	inlines = [TrackInLine, AlbumInLine]

admin.site.register(Artist, ArtistAdmin)
