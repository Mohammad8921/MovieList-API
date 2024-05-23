from django.urls import path, include
from watchlist_app.api.views import WatchListAV, MovieDetailsAV, StreamPLatformAV

urlpatterns = [
    path('movies/list/', WatchListAV.as_view(), name='movie-list'),
    path('movies/<int:pk>', MovieDetailsAV.as_view(), name='movie-details'),
    path('platforms/list/', StreamPLatformAV.as_view(), name='stream-platform')
]
