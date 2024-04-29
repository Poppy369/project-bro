from django.urls import path
from . import views


urlpatterns = [
    path('',views.dataSearch,name='dataSearch'),
    path('dataForm',views.dataForm, name='dataForm')
]
