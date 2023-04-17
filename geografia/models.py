from django.db import models

# Create your models here.

class Pais(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    nombre = models.CharField(max_length=50)
    numero_habitantes = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "{}".format(self.nombre)

    class Meta:
        db_table = 'pais'  # Especificar el nombre de la tabla que se creara en la migración
        verbose_name        = "Pais"  # Manipular nombre en el panel
        verbose_name_plural = "Paises"  # Manipular nombre en el panel

class Ciudad(models.Model):  # Modelo creado para ejecutar migraciones
    # Definir los datos de la clase (campos de la tabla)
    # Si no se especifica lo contrario, todos los campos seran requeridos por defecto, es decir NOT NULL
    nombre = models.CharField(max_length=100)
    alcalde = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} ({})".format(self.nombre, self.pais.nombre)

    class Meta:
        db_table = 'ciudad'  # Especificar el nombre de la tabla que se creara en la migración
        verbose_name        = "Ciudad"  # Manipular nombre en el panel
        verbose_name_plural = "Ciudades"  # Manipular nombre en el panel
