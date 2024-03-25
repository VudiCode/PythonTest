from django.http import HttpResponse
from .forms import MyForm, HelloForm
from django.shortcuts import render
from .models import Person

def index(request):
    return HttpResponse("Hello, world!")

def my_view(request):
    form = MyForm()
    return render(request, 'my_template.html', {'form': form})

def hello_world(request):
    if request.method == 'POST':
        form = HelloForm(request.POST)
        if form.is_valid():
            userName = form.cleaned_data['name']
            userEmail = form.cleaned_data['email']
            # Делайте что-то с данными формы, например, сохраняйте их в базу данных

            person = Person(name=userName, email=userEmail)
            person.save()

    else:
        form = HelloForm()
    return render(request, 'hello.html', {'form': form})