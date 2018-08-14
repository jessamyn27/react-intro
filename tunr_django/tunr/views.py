from django.shortcuts import render
# THIS IS LIKE OUR CONTROLLER IN EXPRESS

# Create your views here.
from .models import Artist, Song

# this is our db query like saying artist.find in mongoose

# we are injecting this indo our db with a template we have not created yet that will render when this function is called

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})
