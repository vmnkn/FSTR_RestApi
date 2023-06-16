from django.urls import path
from .views import PerevalList, submit_data, get_data

urlpatterns = [
    path('submitData/', PerevalList.as_view(), name='pereval_list'),
    path('submitData/create/', submit_data, name='submit_data'),
    path('submitData/<int:pk>/', get_data, name='get_data'),
]
