from django.urls import path
from . import views

# MY NOTES: THIS IS OUR ROOT URL SIMILAR TO USING '/'

#  first part is calling the function in our views second part is what is going in our template which needs to be in a template folder and this object 'artists' will render

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('songs/', views.song_list, name='song_list'),
]
