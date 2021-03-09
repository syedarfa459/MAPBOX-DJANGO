from django.shortcuts import render
from .forms import PlaceForm


# Create your views here.
def home_map(request):
    fm = PlaceForm()
    if request.method == 'POST':
        fm = PlaceForm(request.POST)
        if fm.is_valid():
            fm.save()
    return render(request, 'maps/index.html', context={'form': fm})
