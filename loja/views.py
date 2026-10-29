from django.shortcuts import render, get_object_or_404,redirect
from loja.models import Produto

def index(request):
    
    produtos = Produto.objects.filter(publicada=True)
    return render(request,'loja/index.html', {"cards": produtos})