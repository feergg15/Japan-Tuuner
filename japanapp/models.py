from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telefono = PhoneNumberField(unique=True, null=True, blank=False,region="ES",default="")
    email = models.EmailField(max_length=70,blank=True,unique=True) 
    avatar = models.ImageField(upload_to='img', height_field=None, blank=True,null=True)
    # def get_absolute_url(self):
    #     return reverse('japanapp:coche-detalle', kwargs={'pk': self.pk})
    # REQUIRED_FIELDS = ["telefono", "email" , "avatar"]
    

class Coche(models.Model):
    #marca = models.TextChoices=("Marca" , "MA") Para que el usuario pueda permitir escribir la marca de un coche
    año = models.DateField()
    marca = models.CharField(max_length=20, null=True)
    modelo = models.CharField(max_length=20)
    estilo = models.CharField(max_length=20, null=True)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.marca} | {self.modelo}"
    def get_absolute_url(self):
        return reverse("coche-detalles", kwargs={"pk": self.pk})


class Escape(models.Model):
    marca = models.CharField(max_length=20, null=True)
    modelo_escape =  models.CharField(max_length=20, null=True)
    modelo_coche =  models.ForeignKey(Coche, on_delete=models.CASCADE) #Cada escape pertenece a un modelo de coche , un coche solo puede tener un escape por proyecto
    material = models.CharField(max_length=20, null=True)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.marca} | {self.modelo_escape}"
    def get_absolute_url(self):
        return reverse("coche-detalles", kwargs={"pk": self.pk})

class Llanta(models.Model):
    marca = models.CharField(max_length=20, null=True)
    modelo_llanta =  models.CharField(max_length=20, null=True)
    modelo_coche =  models.ForeignKey(Coche, on_delete=models.CASCADE)
    color =  models.CharField(max_length=20, null=True)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.marca} | {self.modelo_llanta}"
    def get_absolute_url(self):
        return reverse("llanta-detalles", kwargs={"pk": self.pk})

class Volante(models.Model):
    marca = models.CharField(max_length=20, null=True)
    modelo_volante =  models.CharField(max_length=20,null=True)
    modelo_coche =  models.ForeignKey(Coche, on_delete=models.CASCADE)
    material =  models.CharField(max_length=20, null=True)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.marca} | {self.modelo_volante}"
    def get_absolute_url(self):
        return reverse("volante-detalles", kwargs={"pk": self.pk})


class Body_Kit(models.Model):
    marca = models.CharField(max_length=20, null=True)
    modelo_bk =  models.CharField(max_length=20,null=True)
    modelo_coche =  models.ForeignKey(Coche, on_delete=models.CASCADE)
    material =  models.CharField(max_length=20, null=True)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.marca} | {self.modelo_bk}"
    def get_absolute_url(self):
        return reverse("bk-detalles", kwargs={"pk": self.pk})


class Suspension(models.Model):
    marca = models.CharField(max_length=20, null=True)
    modelo_suspes =  models.CharField(max_length=20,null=True)
    modelo_coche =  models.ForeignKey(Coche, on_delete=models.CASCADE)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.marca} | {self.modelo_suspes}"
    def get_absolute_url(self):
        return reverse("suspension-detalles", kwargs={"pk": self.pk})

class Filtro(models.Model):
    marca = models.CharField(max_length=20, null=True)
    modelo_filtro =  models.CharField(max_length=20,null=True)
    modelo_coche =  models.ForeignKey(Coche, on_delete=models.CASCADE)
    material =  models.CharField(max_length=20, null=True)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.marca} | {self.modelo_filtro}"
    def get_absolute_url(self):
        return reverse("Filtro-detalles", kwargs={"pk": self.pk})
        
class Proyecto(models.Model):
    usuario = models.ForeignKey(User, related_name="usuario", on_delete=models.CASCADE,default=1)
    modelo_coche = models.ForeignKey(Coche, related_name="Modelo_Coche", on_delete=models.CASCADE)
    modelo_escape = models.ForeignKey(Escape,related_name="Modelo_escape", on_delete=models.CASCADE)
    modelo_llanta = models.ForeignKey(Llanta,related_name="Modelo_llanta", on_delete=models.CASCADE)
    modelo_volante = models.ForeignKey(Volante,related_name="Modelo_volante", on_delete=models.CASCADE)
    modelo_bk = models.ForeignKey(Body_Kit,related_name="Modelo_bk", on_delete=models.CASCADE)
    modelo_suspes = models.ForeignKey(Suspension, related_name="Modelo_suspension", on_delete=models.CASCADE)
    modelo_filtro = models.ForeignKey(Filtro, related_name="Modelo_filtro", on_delete=models.CASCADE)
    img = models.ImageField("foto", height_field=None, blank=True,null=True)
    def __str__(self):
        return f"{self.pk} | {self.modelo_coche}"
    def get_absolute_url(self):
        return reverse("proyecto-list", kwargs={"pk": self.pk})

# class Usuario(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     PhoneNumber = PhoneNumberField(unique=True, null=True, blank=False,region="ES",default="")
#     email = models.EmailField(max_length=70,blank=True,unique=True) 
#     avatar = models.ImageField(upload_to='img', height_field=None, blank=True,null=True)