from django.db import models
from django.utils import timezone

# Create your models here.
class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100)
    def __str__(self):
        return self.marca
    



class Edad(models.Model):
    id = models.AutoField(primary_key=True)
    edad = models.CharField(max_length=100)
    def __str__(self):
        return self.edad
    



class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    direccion = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    



class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.CharField(max_length=100)
    def __str__(self):
        return self.categoria
    



class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    def __str__(self):
        return self.direccion

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    consumidor = models.CharField(max_length=100)
    def __str__(self):
        return self.consumidor
    
class Tamaño(models.Model):
    id=models.AutoField(primary_key=True)
    tamaño=models.CharField(max_length=100,verbose_name="Tamaño")
    def __str__(self) -> str:
        return self.tamaño
    
class Consistencia(models.Model):
    id = models.AutoField(primary_key=True)
    consistencia = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.consistencia

class Animal(models.Model):
    id = models.AutoField(primary_key=True)
    animal = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.animal
    
    

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey('Categoria', null=True, blank=False, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=100)
    animal = models.ForeignKey('Animal', null=True, blank=False, on_delete=models.CASCADE)
    tamaño = models.ForeignKey('Tamaño', null=True, blank=False, on_delete=models.CASCADE)
    edad=models.ForeignKey('Edad', null=True, blank=False, on_delete=models.CASCADE)
    marca = models.ForeignKey('Marca', null=True, blank=False, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock_a=models.IntegerField(verbose_name='Stock Actual')
    stock_r=models.IntegerField(verbose_name='Stock Reposicion', default=0, null=True, blank=True)
    stock_m=models.IntegerField(verbose_name='Stock Minimo')
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    consis = models.ForeignKey('Consistencia', null=True, blank=True, on_delete=models.CASCADE)
    obs = models.CharField(max_length=150, verbose_name='Observaciones', default='')
    des = models.TextField(verbose_name='Descripcion', default='')
    def __str__(self):
        return self.nombre
class Caja(models.Model):
    id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey('empleado', null=True, blank=False, on_delete=models.CASCADE)
    sucursal = models.ForeignKey('sucursal', null=True, blank=False, on_delete=models.CASCADE)
    abierta = models.BooleanField(default=True, verbose_name='Caja Abierta')
    fecha_hs_ap = models.DateTimeField(default=timezone.now, verbose_name='Fecha y hora de apertura')
    fecha_hs_cier = models.DateTimeField(null=True, blank=True, verbose_name='Fecha y hora de cierre') 
    monto_ini = models.FloatField(verbose_name='Monto Inicial')
    total_ing = models.FloatField(verbose_name='Total Ingresos')
    total_egr = models.FloatField(verbose_name='Total Egresos')

    def cerrar_caja(self):
        self.fecha_hs_cier = timezone.now()
        self.abierta = False
        self.save()


    


