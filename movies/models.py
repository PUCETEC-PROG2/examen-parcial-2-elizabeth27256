from django.db import models

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True) 
    title_movie = models.CharField(max_length=255)  
    genero_movie = models.CharField(max_length=100)  
    name = models.CharField(max_length=255)  
    date = models.DateField(),
    synopsis = models.TextField()  
    def __str__(self):
        return self.title
