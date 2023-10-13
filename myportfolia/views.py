from django.shortcuts import render

# Create your views here.

def HomePageViews(request):
    return render(request, 'index.html')
