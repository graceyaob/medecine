from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length= 200)
    prenom = models.CharField(max_length= 200)
    email = models.EmailField()
    date_de_naissance = models.DateField()

    def __str__(self):
        return f'{self.nom} {self.prenom}'
    



    
    
