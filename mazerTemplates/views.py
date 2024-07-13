from django.shortcuts import render

def homepage(request):
    context = {}
    return render(request, 'mazerTemplates/index.html', context)
# Create your views here.
