from rest_framework import serializers

from .models import Artist

class ArtistSerializer(serializers.HyperlinkedModelSerializer):

	es_ff1 = serializers.SerializerMethodField('es_ff2')

	filter_fields = ('id', )

	def es_ff2(self, obj):
		return obj.es_ff()

	class Meta:
		model = Artist
		fields = ('id', 'first_name', 'last_name', 'es_ff1')