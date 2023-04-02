from django.shortcuts import render, redirect
from .forms import CreateUserForm

# Create your views here.

def home(request):

    return render(request, 'index.html')


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("")
        
    context = {'form': form}

    return render(request, 'register.html', context=context)


def dashboard(request):

    return render(request, 'dashboard.html')