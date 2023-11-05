from django.shortcuts import render

# Create your views here.
def home_view(request):
    title = 'Welcome to Django'
    return render(request, "base.html", {'title' : title})