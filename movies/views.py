from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Movie, Watchlist
from .serializers import MovieSerializer, WatchlistSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def watchlist_view(request):
    if request.method == 'GET':
        watchlist = Watchlist.objects.filter(user=request.user)
        serializer = WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        movie_id = request.data.get('movie_id')
        try:
            movie = Movie.objects.get(id=movie_id)
            watchlist, created = Watchlist.objects.get_or_create(user=request.user, movie=movie)
            if created:
                return Response({'message': 'Added to watchlist'}, status=status.HTTP_201_CREATED)
            return Response({'message': 'Already in watchlist'}, status=status.HTTP_200_OK)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_watchlist(request, movie_id):
    try:
        watchlist = Watchlist.objects.get(user=request.user, movie_id=movie_id)
        watchlist.delete()
        return Response({'message': 'Removed from watchlist'}, status=status.HTTP_200_OK)
    except Watchlist.DoesNotExist:
        return Response({'error': 'Not in watchlist'}, status=status.HTTP_404_NOT_FOUND)