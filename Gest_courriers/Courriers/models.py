from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline=models.DateField()
    date_enregistrement=models.DateField()
    commentaire=models.TextField()
    objet=models.TextField()
    situation=models.TextField()
    n_courrier = models.CharField(max_length=2000)
    source=models.CharField(max_length=2000)
    date_reception=models.DateField()
    nature=models.CharField(max_length=100)
    def __str__(self):
        return self.n_courrier

	
	
	
	
    
	
		
