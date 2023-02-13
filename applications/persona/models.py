from django.db import models
from applications.departamento.models import Departamento

from ckeditor.fields import RichTextField



class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleado'

    def __str__(self):
        return str(self.id) +'-'+ self.habilidad



class Empleado(models.Model):
    """Modelo para la tabla empleado"""
    JOB_CHOICES =(
        ('0','programador'),
        ('1', 'CONTADOR'),
        ('2', 'Admistrado'),
        ('3', 'Economista'),
        ('4', 'Doctora'),
        ('5', 'Otro'),
    )

    # programador
    # Admistrado
    # Economista
    # Doctora
    # Otro

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellido', max_length=60)

    full_name = models.CharField(
        'Nombres completos',
        max_length=60,
        blank=True

        )

    avatar = models.ImageField(upload_to= 'empleado', blank=True, null=True)
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()
    

    class Meta:
        verbose_name_plural = 'Empleados de la empresa'
        ordering = ['first_name']
        unique_together = ('first_name', 'departamento')
        

    def __str__(self):
        return str(self.id) + '-' + self.first_name +'-'+ self.last_name

    