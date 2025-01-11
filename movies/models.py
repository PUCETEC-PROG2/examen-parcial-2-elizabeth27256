from django.db import models

class Movie(models.Model):
    movie_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title_movie = models.CharField(max_length=30)  
    genero_movie = models.CharField(max_length=30)  
    name = models.CharField(max_length=500)  
    date = models.DateField(),
    synopsis = models.TextField()  
    def __str__(self):
        return self.title
