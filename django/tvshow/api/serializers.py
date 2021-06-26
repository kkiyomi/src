from rest_framework import serializers
from tvshow.models import *


class ReleaseV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseV2
        fields = ['id', 'number', 'link', 'date_added']
        depth = 1


class TVShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ['id', 'title', 'slug', 'image']
        depth = 1


class TVShowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ['id', 'title', 'description', 'year', 'image', 'slug']
        depth = 1
        lookup_field = 'slug'


class TVShowAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ['title', 'description', 'year', 'genre', 'image']


class ReleaseAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReleaseV2
        fields = ['tvshow', 'number', 'link']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']


class TVShowStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TVShow
        fields = ['state']
