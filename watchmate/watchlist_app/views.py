'''
from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse
# Create your views here.

def MovieList(request):
    movies = Movie.objects.all()
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)

def MovieDetails(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        pk: {
            'name': movie.name,
            'des': movie.description,
            'active': movie.active
        }
    }
    return JsonResponse(data)
'''
    