from django.urls import path, include
from watchlist_app.api.views import WatchListAV, MovieDetailsAV, StreamPlatformAV, ReviewAV, ReviewDetailsAV, ReviewCreateAV, WatchListGV

urlpatterns = [
    path('movies/list/', WatchListAV.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailsAV.as_view(), name='movie-details'),
    path('platforms/list/', StreamPlatformAV.as_view(), name='stream-platform'),
    path('movies/<int:pk>/reviews/', ReviewAV.as_view(), name='movie-reviews'),
    path('movies/reviews/<int:pk>/', ReviewDetailsAV.as_view(), name='review-details'),
    path('movies/<int:pk>/review-create/', ReviewCreateAV.as_view(), name='review-create'),
    path('movies/list2/', WatchListGV.as_view(), name='watchlist-search')
]
