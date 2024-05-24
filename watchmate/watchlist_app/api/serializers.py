from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review
    
class WatchListSerializer(serializers.ModelSerializer):
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):
    name_len = serializers.SerializerMethodField()
    watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatform
        fields = "__all__"
        
    def get_name_len(self, object):
        return len(object.name)   

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        
               
'''
class MovieSerializer(serializers.Serializer):
    id  = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.CharField()
    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data) 
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
'''        