from django.shortcuts import render

def index(request):
    """The home page for High Plains HEMA."""
    return render(request, 'high_plains_hema/index.html')
