from django.urls import path
from  .views import universitet_list

urlpatterns = [
    path('', universitet_list, name ='universitet_list')

]
