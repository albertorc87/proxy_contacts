from django.db import models
import datetime

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

class ExtensionContacto(Contacto):
    class Meta:
        proxy = True
        ordering = ["apellidos"]


    def get_datos_contacto(self):
        # print('El contacto se llama {} y sus apellidos son {}'.format(self.nombre, self.apellidos))
        return self.nombre + ' ' + self.apellidos


    def get_edad(self):
        today = datetime.date.today()
        y = self.fecha_nacimiento.year
        m = self.fecha_nacimiento.month
        d = self.fecha_nacimiento.day
 
        edad = today.year - y

        if(m > today.month):
            edad = edad - 1
        elif(m == today.month and d > today.day):
            edad = edad - 1

        # print('La edad del contacto {} es {}'.format(self.nombre, edad))
        return edad