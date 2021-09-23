from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def inicio(request):
    return redirect('/shows')

def shows(request):
    context ={
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def create_show(request):
    return render(request, 'create_show.html')


def add_show(request):
    Show.objects.create(
        title=request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['r_date'],
        description = request.POST['description'],
        )
    return redirect('/shows')


def tv_show(request, show_id):
    context = {
    'tv_show': Show.objects.get(id=show_id)
    }
    return render(request, 'tv_show.html', context)


def edit_show(request, show_id):
    context = {
    'tv_show': Show.objects.get(id=show_id)
    }
    return render(request, 'edit_show.html', context)


def update_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['ed_title']
    show.network = request.POST['ed_network']
    show.release_date = request.POST['ed_r_date']
    show.description = request.POST['ed_description']
    show.save()
    return redirect(f'/shows/{show_id}/')

def del_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')