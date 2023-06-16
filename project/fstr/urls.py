from django.urls import path
from .views import PerevalList, submit_data, get_data, update_data

urlpatterns = [
    path('submitData/', PerevalList.as_view(), name='pereval_list'),
    path('submitData/create/', submit_data, name='submit_data'),
    path('submitData/<int:pk>/', get_data, name='get_data'),
    path('submitData/<int:pk>/update/', update_data, name='update_data'),
]
