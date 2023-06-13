from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('latitude',
                  'longitude',
                  'height', )


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter',
                  'summer',
                  'autumn',
                  'spring', )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email',
                  'fam',
                  'name',
                  'otc',
                  'phone', )


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('image',
                  'title', )


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ('beauty_title',
                  'title',
                  'other_titles',
                  'connect', )


class PerevalAddSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    perevals = PerevalSerializer()
    coordinates = CoordinatesSerializer()
    level = LevelSerializer()
    image = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = ('id',
                  'user',
                  'perevals',
                  'coordinates',
                  'level',
                  'image',
                  'status', )

    def create(self, validated_data):
        image_data = validated_data.pop('image')
        pereval = Pereval.objects.create(**validated_data)
        for image in image_data:
            Images.objects.create(pereval=pereval, **image)
        return pereval
