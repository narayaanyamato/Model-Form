from django.shortcuts import render
from modelformapp.forms import Movieform
from modelformapp.models import Movie
def view_movie(request):
    return render(request,'Pages/index.html')

def Add_movie(request):
    submit=False
    if(request.method=='POST'):
        obj=Movieform(request.POST)
        if(obj.is_valid()):
            obj.save(commit=True)
            print("data sumited...")
            
    obj=Movieform()
    return render(request,'Pages/addmovie.html',{"obj":obj,"submit":submit})    

def view_movielist(request):
    movie_list=Movie.objects.all()
    
    return render(request,'Pages/viewmovies.html',{"movie_list":movie_list})     

def submit(request):
    return render(request,'Pages/submit.html')       
