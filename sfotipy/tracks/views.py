import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


from .models import Track
@login_required
def track_view(request, title):

	track = get_object_or_404(Track,title=title)

	data = {
		'title': track.title,
		'order':track.order,
		'album':track.album.title,
		'artist':{
			'name': track.artist.first_name,
			'bio': track.artist.biography,
		}
	}

	json_data = json.dumps(data)

	#return HttpResponse(json_data, content_type='application/json')

	return render(request, 'track.html', {'track':track})



from rest_framework import viewsets
from .serializers import TrackSerializer

class TrackViewSet(viewsets.ModelViewSet):
	model = Track
	queryset = Track.objects.all()
	serializer_class = TrackSerializer
