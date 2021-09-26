from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def inicio(request):
    return redirect('/shows')

def shows(request):
    context ={
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)


def create_show(request):
    context = {
    'today': str(date.today())
    }
    return render(request, 'create_show.html', context)


def add_show(request):
    errores = Show.objects.basic_validator(request.POST)
    if len(errores) > 0:
        for key, value in errores.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:
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
    errores = Show.objects.basic_validator(request.POST)
    if len(errores) > 0:
        for key, value in errores.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['r_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show_id}/')

def del_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')