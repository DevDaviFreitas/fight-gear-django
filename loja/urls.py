from django.urls import path
from loja.views import index

urlpatterns = [
    path('', index, name='index'),
]