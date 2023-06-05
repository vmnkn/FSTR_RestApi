from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, AbstractBaseUser
from django.db import connection
from django.apps import AppConfig


class PerevalAdded(models.Model):
    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    STATUS_CHOICES = [
        ('new', 'новый'),
        ('pending', 'модератор взял в работу'),
        ('accepted', 'модерация прошла успешно'),
        ('rejected', 'информация не принята'),
    ]

    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=NEW)
    beauty_title = models.CharField(max_length=128, verbose_name='Препядствие')
    title = models.CharField(max_length=128, verbose_name='Вершина')
    other_titles = models.CharField(max_length=128, verbose_name='Другое название')
    connect = models.TextField(null=True)
    add_time = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    coordinates = models.ForeignKey('Coordinates', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.beauty_title} {self.title} {self.other_titles} id: {self.pk}'

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевал'


class Coordinates(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


class Level(models.Model):
    winter = models.CharField(max_length=16, verbose_name='Зима', null=True)
    summer = models.CharField(max_length=16, verbose_name='Лето', null=True)
    autumn = models.CharField(max_length=16, verbose_name='Осень', null=True)
    spring = models.CharField(max_length=16, verbose_name='Весна', null=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'

    class Meta:
        verbose_name = 'Уровень сложности'
        verbose_name_plural = 'Уровень сложности'


class Images(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображение', null=True)
    title = models.CharField(max_length=128)
    add_time = models.DateField(auto_now_add=True)

    pereval = models.ForeignKey(PerevalAdded, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'id: {self.pk}, {self.title}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображение'


phone_number = RegexValidator(
    regex=r'^\+?1?\d{9,12}$',
    message='Номер должен быть введен в формате: '
            '"+79361233454".'
)


class Users(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    otc = models.CharField(max_length=128)
    phone = models.CharField(validators=[phone_number], max_length=16, blank=True)

    def __str__(self):
        return f'{self.fam} {self.name} {self.otc}'
