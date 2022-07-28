from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def counter(request):
    words = request.POST['text']
    number = len(words.split())
    return render(request, 'counter.html', {'number': number})

