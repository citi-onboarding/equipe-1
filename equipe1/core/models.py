from django.db import models
from django.contrib.auth.models import (PermissionsMixin, UserManager)
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUserManager(UserManager):
    def create_user(self, username, password,**extra_fields):
    

        user = self.model(username=username,**extra_fields)

        
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, password,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.model(username=username,**extra_fields )

        user.set_password(password)
        user.save(using=self._db)
        return user



class Casa(models.Model):
    titulo = models.CharField(max_length=100)
    valor = models.FloatField()
    endereco = models.CharField(max_length=140)
    data_adicao = models.DateField(auto_now=True) #vai ter argumento?
    foto = models.FileField(upload_to='oi/') #botar o caminho da pasta onde vao ficar as imagens
    usuario = models.CharField(max_length=50)
    disponibilide = models.BooleanField
    descricao = models.CharField(max_length=200)
    codigo = models.AutoField(primary_key=True)

    def __str__(self):
        return self.titulo

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=10000)
    telefone = models.CharField(max_length=42)
    casas = models.ManyToManyField(Casa)
    is_active = models.BooleanField(_('ativo'), default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')




