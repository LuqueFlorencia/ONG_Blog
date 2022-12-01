from django.urls import path, include
from . import views

app_name = 'noticias'

urlpatterns = [

    path('', views.listar_Noticias, name ='listar'),

]