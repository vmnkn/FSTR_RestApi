from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = ('latitude',
                  'longitude',
                  'height', )
        verbose_name = 'Координаты'


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter',
                  'summer',
                  'autumn',
                  'spring', )
        verbose_name = 'Уровень сложности'


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='first_name')
    fam = serializers.CharField(source='last_name')
    otc = serializers.CharField(source='patronymic')
    email = serializers.CharField()
    phone = serializers.CharField()

    class Meta:
        model = User
        fields = ('email',
                  'fam',
                  'name',
                  'otc',
                  'phone', )
        verbose_name = 'Пользователь'


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Images
        fields = ('image',
                  'title', )
        verbose_name = 'Изображение'


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
