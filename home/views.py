from django.shortcuts import render,redirect
from home.forms import UserForm
from home.models import User
import sys

# Create your views here.

def show(request):
    data = User.objects.all()
    return render(request,'index.html',{'d':data})

def home(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/home')
            except:
                print('------------------------', sys.exc_info())

    else:
        form = User()

    return render(request, 'home.html', {'form': form})

def edit(request, id):
    ui = User.objects.get(u_id = id)
    form = UserForm(request.POST, instance=ui)
    if form.is_valid():
        form.save()
        return redirect('/data')
    return render(request, 'edit.html', {'ui':ui})

def delete(request, id):
    ei = User.objects.get(u_id=id)
    ei.delete()
    return redirect('/data')

