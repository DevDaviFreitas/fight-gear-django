from django.db import models
from datetime import datetime

# Create your models here.
class Produto(models.Model):
    
    OPCOES_CATEGORIA = [("LUVA","Luva" ),("CANELEIRA","Caneleira" ),("PROTETOR BUCAL","Protetor bucal" )]
    
    
    nome = models.CharField(max_length=100, null=False,blank=False)
    categoria = models.CharField(max_length=100,choices= OPCOES_CATEGORIA, default="")
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now,blank=False)
    
    def __str__(self):
        return self.nome