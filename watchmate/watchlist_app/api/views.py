from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins

class ReviewAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class ReviewDetailsAV(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
       
class StreamPlatformAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class WatchListAV(APIView):
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class MovieDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': f'Movie {pk} Does not exist'}, status=status.HTTP_404_NOT_FOUND)
        serialzier = WatchListSerializer(movie)
        return Response(serialzier.data)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serialzier = WatchListSerializer(movie, data=request.data)
            if serialzier.is_valid():
                serialzier.save()
                return Response(serialzier.data)
            else:
                return Response(serialzier.errors)
        except WatchList.DoesNotExist:
            return Response({'Error': f'Movie {pk} Does not exist'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response({'SUCCESS': f'Movie {pk} successfully deleted.'}, status=status.HTTP_204_NO_CONTENT)
        except WatchList.DoesNotExist:
            return Response({'Error': f'Movie {pk} Does not exist'}, status=status.HTTP_404_NOT_FOUND)

'''
class StreamPlatformAV(APIView):
    def get(self, request):
        platforms = StreamPLatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
'''    