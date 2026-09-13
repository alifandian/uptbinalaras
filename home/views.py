from django.shortcuts import render

# Create your views here.
# Halaman index / landing page SIMAPAURI
def index(request):
    return render(request, "home/index.html")