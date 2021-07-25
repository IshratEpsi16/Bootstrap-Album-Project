from django.shortcuts import render
from . models import album_db
# Create your views here.
def index(request):
    album_loop = album_db.objects.all()
    context = {'album_loop' : album_loop}
    return render(request,'album_app/index.html',context)