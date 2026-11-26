from django.shortcuts import render

def home(request):
    return render(request, 'loja/index.html')
# Create your views here.
