from django.db import models

class Animal (models.Model):
    PORTE_DO_ANIMAL = (
        ('P', 'Pequeno'),
        ('M', 'Medio'),
        ('G', 'Grande'),
    )
    ESPECIE_DO_ANIMAL = (
        ('GT','Gato'),
        ('CH', 'Cachorro'),
        ('PS', 'Passaro'),
    )
    caracteristica = models.TextField ()
    porte_do_animal = models.CharField (max_length=1, choices= PORTE_DO_ANIMAL, blank=False, null=False)
    especie_do_animal = models.CharField (max_length=2, choices= ESPECIE_DO_ANIMAL, blank=False, null=False)

    def __str__ (self):
        return self.especie_do_animal

class Services (models.Model):
    BANHO = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    TOSA = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    servicos_medicos = models.TextField 
    banho = models.CharField (max_length=1, choices= BANHO, blank=False, null=False)
    tosa= models.CharField (max_length= 1, choices= TOSA, blank=False, null=False)

    def __str__ (self):
        return self.servicos_medicos

# Create your models here.
