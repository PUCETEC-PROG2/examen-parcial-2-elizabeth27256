from django.shortcuts import render, get_object_or_404
from .models import Movie


def list_movies(request):
    peliculas = Movie.objects.all()  
    return render(request, 'index.html', {'peliculas': peliculas})  

def details_movie(request, id):
    pelicula = get_object_or_404(Movie, pk=id)
    return render(request, 'details_movies.html', {'pelicula': pelicula})