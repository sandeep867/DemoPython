from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import List
from .forms import MovieForm


# Create your views here.


def index(request):
    movie = List.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, "index.html", context)


def info(request, movie_id):
    movie = List.objects.get(id=movie_id)
    return render(request, "info.html", {'film': movie})


def add_movie(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        des = request.POST.get('des')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = List(name=name, des=des, year=year, img=img)
        movie.save()
        return redirect('/')
    return render(request,'add.html')


def update(request, id):
    movie = List.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'form': form})


def delete(request, id):
    if request.method == 'POST':
        movie = List.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')
