from django.db import models 
from django.contrib.auth.models import PermissionsMixin 
from django.contrib.auth.base_user import AbstractBaseUser 
from django.utils.translation import ugettext_lazy as _ 
from django.contrib.auth.base_user import BaseUserManager 

#Tipos de usuario que existen en el sistema 
USER_TYPE_CHOICES = ( 
      (1, 'usuario'), 
      (2, 'encargado'), 
      (3, 'supervisor'),
      (4, 'admin'), 
  ) 
 
class UserManager(BaseUserManager): 
    ''' 
    Clase de manager del usuario 
    Se encargará de manejar el “query set” del User Model 
    ''' 
    use_in_migrations = True 
 
    def _create_user(self, email, password, **extra_fields): 
        """ 
        Creates and saves a User with the given email and password. 
        """ 
        if not email: 
            raise ValueError('The given email must be set') 
        email = self.normalize_email(email) 
        user = self.model(email=email, **extra_fields) 
        user.set_password(password) 
        user.save(using=self._db) 
        return user 
 
    def create_user(self, email, password=None, **extra_fields): 
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('tipo',1)
        return self._create_user(email, password, **extra_fields) 
 
    def create_superuser(self, email, password, **extra_fields): 
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('tipo',4)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.') 
 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True.') 
 
        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin): 
    '''  
    Clase de usuario del sistema  
    ''' 
    nombre = models.CharField(max_length=50, null=True, blank=True) 
    rut = models.CharField(max_length=15, null=True, unique=True, blank=True) 
    num_documento = models.CharField(max_length=15, null=True, unique=True, blank=True) 
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True) 
    apellido_paterno = models.CharField(max_length=50, null=True, blank=True) 
    apellido_materno = models.CharField(max_length=50, null=True, blank=True) 
    email = models.EmailField(_('email address'), unique=True, blank=False) 
    tipo = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1) 
    username = models.CharField(max_length=50, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_funcionario = models.BooleanField(default=False)
    objects = UserManager()
    
    USERNAME_FIELD = 'email' 
 
    REQUIRED_FIELDS = ['rut','nombre','apellido_paterno','apellido_materno'] 
 
    class Meta: 
        verbose_name = _('usuario') 
        verbose_name_plural = _('usuarios') 
    

    def get_full_name(self): 
        ''' 
        Retorna el nombre completo 
        ''' 
        full_name = '%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno) 
        return full_name.strip() 
 
    def get_short_name(self): 
        ''' 
        Returns the short name for the user. 
        ''' 
        return self.nombre 
    
    
 