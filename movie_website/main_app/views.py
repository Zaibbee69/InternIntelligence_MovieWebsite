from django.shortcuts import render
from django.http import HttpResponse
from api.tmdb_api import get_popular_movies

# Create your views here.

def index(request):
    movies = get_popular_movies()
    return render(request, "main_app/index.html", {
        "movies": movies
    })