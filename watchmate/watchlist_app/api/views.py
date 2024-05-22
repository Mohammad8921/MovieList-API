from watchlist_app.models import Movie
from rest_framework.decorators import api_view
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def MovieList(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    else:
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])    
def MovieDetails(request, pk):
    if request.method=='GET':
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Error': f'Movie {pk} Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serialzier = MovieSerializer(movie)        
        return Response(serialzier.data)

    elif request.method=='PUT':
        try:
            movie = Movie.objects.get(pk=pk)
            serialzier = MovieSerializer(movie, data=request.data)
            if serialzier.is_valid():
                serialzier.save()
                return Response(serialzier.data)
            else:
                return Response(serialzier.errors)
        except Movie.DoesNotExist:
            return Response({'Error': f'Movie {pk} Does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({'SUCCESS': f'Movie {pk} successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response({'Error': f'Movie {pk} Does not exist'}, status=status.HTTP_404_NOT_FOUND)            
        
        
    

    
        