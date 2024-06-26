from django.shortcuts import render

def index (request):
    context={}
    return render(request, 'tienda/index.html', context)