from django.shortcuts import render


# Create your views here.

def dashboard(request):
    return render(request, 'blog/home.html', {'title': 'Dashboard'})

def about(request):
    return render(request, 'blog/about.html')

