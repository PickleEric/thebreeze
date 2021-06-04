from django.shortcuts import render

def homepage(request):
    return render(request, 'thebreeze_app/home.html')
