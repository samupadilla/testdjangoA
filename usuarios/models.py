from django.db import models

# Create your models here.
class Aprendiz(models.Model):

    genero_eleccion=(
        ('M','Masculino'),
        ('F','Femenino'),
        ('NR','No responde')
    )
    #Django tiene por default campo id 
    name=models.CharField(max_length=100)
    #photo=models.ImageField(upload_to='photos/%Y/%m/%d/', default='', blank=True)
    photo=models.ImageField(upload_to='foticos/')
    sureName=models.CharField(max_length=100)
    documento=models.IntegerField()    
    genero=models.CharField(choices=genero_eleccion,max_length=100)
    ficha=models.IntegerField()
    

    def __str__(self):
        return self.name