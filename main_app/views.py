from django.shortcuts import render
plants = [
    {'name': 'Monstera Deliciosa', 'common_name': 'swiss cheese plant', 'family': 'Araceae'},
    {'name': 'Ficus benjamin','common_name': 'Weeping Fig','family': 'Moraceae'},
    {'name': 'Ficus Lyrata','common_name': 'Fiddle-Leaf Fig','family': 'Moraceae'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    return render(request, 'plants/index.html', {'plants' : plants})