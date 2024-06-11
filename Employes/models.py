from django.db import models
from django.core.validators import MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField
from .choices import  Oficinas_ordenadas, Status_ordenadas, Cargos_ordenadas, Dependencias_ordenadas


class Estados(models.Model):
    codEstado = models.AutoField(primary_key=True, unique=True)
    estado = models.CharField('Estado', max_length=30)
    capital = models.CharField('Capital', max_length=30)
    sigla = models.CharField('Sigla', max_length=2, null=True, blank=True)
    def __str__(self):
        return self.estado
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['estado']
        db_table = 'estados'

class Employes(models.Model):
    status = models.CharField('Status', choices=Status_ordenadas, max_length=3, null=True, blank=True
                              
                              
                              )
    cedper = models.CharField('cedula', max_length=9, primary_key=True,validators=[MinLengthValidator(6)])
    nomper = models.CharField('Nombre', max_length=40,validators=[MinLengthValidator(3)])
    apeper = models.CharField('Apellido', max_length=40,validators=[MinLengthValidator(3)])
    telmovper = PhoneNumberField('Telf. Movil',null=True, blank=True, max_length=13)
    dependencia = models.CharField('Ubicacion Admistración', choices=Dependencias_ordenadas, max_length=10)
    oficina = models.CharField('Oficina', choices=Oficinas_ordenadas, max_length=10)
    cargo = models.CharField('Cargo', choices=Cargos_ordenadas, max_length=10, default='DN')
    estado = models.ForeignKey(Estados, verbose_name='Estado', on_delete=models.CASCADE)
    municipio = models.CharField('Municipio', max_length=30)
    parroquia = models.CharField('Parroquia', max_length=30)
    centro = models.CharField('Centro de Votacion',max_length=255, null=True,blank=True)
    votacion= models.BooleanField('Votacion', default=False)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['-cedper']
        db_table = 'employes'
    def __str__(self):
        return f" {self.nomper}  {self.apeper}"