from django.shortcuts import render,redirect
from .forms import MusicianForm, Musician
# Create your views here.
def add_musician(request):
    if request.method== 'POST':
        musician_form= MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
        musician_form= MusicianForm()
    return render(request,'add_musician.html', {'form':musician_form})

def edit_musician(request,id):
    post=Musician.objects.get(pk=id)
    post_form=MusicianForm(instance=post)
    if request.method== 'POST':
        post_form=MusicianForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
    return render(request, 'add_musician.html', {'form': post_form})