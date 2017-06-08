from django.shortcuts import render

# Create your views here. .........
def bucket(request):
    return render(request, 'buck/index_dj.html', {})
