from django.urls import path, include
from watchlist_app.api.views import WatchListAV, MovieDetailsAV, StreamPlatformAV, ReviewAV, ReviewDetailsAV

urlpatterns = [
    path('movies/list/', WatchListAV.as_view(), name='movie-list'),
    path('movies/<int:pk>', MovieDetailsAV.as_view(), name='movie-details'),
    path('platforms/list/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('movies/reviews/', ReviewAV.as_view(), name='movie-reviews'),
    path('movies/reviews/<int:pk>', ReviewDetailsAV.as_view(), name='review-details')
]
