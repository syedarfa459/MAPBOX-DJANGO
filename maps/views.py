from django.shortcuts import render
from .forms import UserLocationForm

# Create your views here.
def home_map(request):

    # mapbox_access_token = 'pk.eyJ1Ijoic3llZGFyZmEiLCJhIjoiY2ttMDM5d2ZsMGkzdjJvcXMwbjhhbHZxYyJ9.2-TETVD32KNkj75LjDq0pg'
    fm = UserLocationForm()

    if request.method == 'POST':
        fm = UserLocationForm(request.POST)
        if fm.is_valid():
            fm.save()
    return render(request, 'maps/index.html', context={'form': fm})


