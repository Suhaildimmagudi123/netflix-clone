from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, watchlist_view, remove_from_watchlist

router = DefaultRouter()
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('watchlist/', watchlist_view, name='watchlist'),
    path('watchlist/<int:movie_id>/', remove_from_watchlist, name='remove_from_watchlist'),
]