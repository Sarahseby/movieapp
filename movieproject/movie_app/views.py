from django.http import HttpResponse
from django.shortcuts import render, redirect
from  . models import Movie
from .forms import MovieForm

# Create your views here.
def index(request):
    movie=Movie.objects.all()
    # context={'movie_list':movie}

    return render(request,'index.html',{'list':movie})

def details(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request, 'detail.html',{'mov':movie})

def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie=Movie(name=name,desc=desc,year=year,img=img)
        movie.save();


    return render(request,'add.html')

def update(requeast,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(requeast.POST or None,requeast.FILES,instance=movie)
    if form.is_valid():
        form .save();
        return redirect('/')
    return render(requeast,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')