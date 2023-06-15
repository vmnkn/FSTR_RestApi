from django.urls import path
from .views import PerevalList, submit_data

urlpatterns = [
    path('submitData/', PerevalList.as_view(), name='pereval_list'),
    path('submitData/create/', submit_data, name='submit_data'),
]
