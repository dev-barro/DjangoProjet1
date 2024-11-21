#from django.contrib import admin
from django.urls import path
# importation des views
from .import views
urlpatterns = [
    path('',views.index,name='index' ),
]