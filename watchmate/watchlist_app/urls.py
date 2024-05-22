'''
from django.urls import path, include
from watchlist_app.views import MovieList, MovieDetails

urlpatterns = [
    path('list/', MovieList, name='movie-list'),
    path('<int:pk>', MovieDetails, name='movie-details')
]
'''