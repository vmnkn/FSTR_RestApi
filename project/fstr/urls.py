from django.urls import path
from .views import PerevalList

urlpatterns = [
    path('submitData/', PerevalList.as_view(), name='pereval_list'),
]
