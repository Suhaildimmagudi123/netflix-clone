from rest_framework import serializers
from .models import Movie, Watchlist


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class WatchlistSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)

    class Meta:
        model = Watchlist
        fields = ['id', 'movie', 'added_at']
