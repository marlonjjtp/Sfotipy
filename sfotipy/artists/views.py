from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from .models import Artist

class ArtistDetailView(DetailView):
	model = Artist

	def get_template_names(self):
		return 'artist.html'

class ArtistListView(ListView):
	model = Artist
	context_object_name = 'artist'
	template_name = 'artists.html'

from rest_framework import viewsets
from .serializers import ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
	model = Artist
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer