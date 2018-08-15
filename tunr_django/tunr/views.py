from django.shortcuts import render, redirect
# THIS IS LIKE OUR CONTROLLER IN EXPRESS

# Create your views here.
from .models import Artist, Song

# this is our db query like saying artist.find in mongoose

# we are injecting this into our db with a template we have not created yet that will render when this function is called

# we are rendering a template. The first argument is the request argument, the second is the template that we want to render, and the third is a dictionary with the data we want to send to the view. In this case, that's the artist QuerySet with the key 'artists'.

# artist index route
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'tunr/artist_list.html', {'artists': artists})

# song index route
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'tunr/song_list.html', {'songs': songs})

# song show route
def song_detail(request, id):
  song = Song.objects.get(id=id)
  return render(request, 'jim/song_detail.html', {'song': song})

# artist show route
def artist_detail(request, pk):
    artist = Artist.objects.get(id=pk)
    return render(request, 'tunr/artist_detail.html', {'artist': artist})

# artist create route for artist_form
def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'tunr/artist_form.html', {'form': form})

# song create route for song_form
def song_create(request):
  if request.method == 'POST':
    form = SongForm(request.POST)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', id=song.id)
  else:
    form = SongForm()
  return render(request, 'jim/song_form.html', {'form': form})

# artist edit route
def artist_edit(request, pk):
  artist = Artist.objects.get(pk=pk)
  if request.method == 'POST':
    form = ArtistForm(request.POST, instance=artist)
    if form.is_valid():
      artist = form.save()
      return redirect('artist_detail', pk=artist.pk)
  else:
    form = ArtistForm(instance=artist)
  return render(request, 'jim/artist_form.html', {'form': form})

# song edit route
def song_edit(request, id):
  song = Song.objects.get(id=id)
  if request.method == 'POST':
    form = SongForm(request.POST, instance=song)
    if form.is_valid():
      song = form.save()
      return redirect('song_detail', id=song.id)
  else:
    form = SongForm(instance=song)
  return render(request, 'jim/song_form.html', {'form': form})

# artist delete route
def artist_delete(request, pk):
  Artist.objects.get(id=pk).delete()
  return redirect('artist_list')

# song delete route
def song_delete(request, id):
  Song.objects.get(id=id).delete()
  return redirect('song_list')
