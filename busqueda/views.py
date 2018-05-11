import os
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from .models import Document
from .forms import DocumentForm


def search(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        # file_ = open(os.path.join(PROJECT_ROOT, uploaded_file_url))
        return render(request, 'search.html', {
            'uploaded_file_url': uploaded_file_url

        })
    return render(request, 'search.html')

def base(request):
    documents = Document.objects.all()
    return render(request, 'base.html', { 
        'documents': documents })
def count_codon():
	text = "Eunice"
	return render(request, 'count_codon.html', { 'text': text })


def porcentaje(request):
    text = "Eunice"
    return render(request, 'porcentaje.html', { 'text': text })
    
def count_base(f):
    with open('django-apps/adn-busqueda/test', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def total_base():
    f = open("django-apps/adn-busqueda/test", "r")
    text = f.read()
    return text