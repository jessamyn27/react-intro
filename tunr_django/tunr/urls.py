from django.urls import path
from . import views

# MY NOTES: THIS IS OUR ROOT URL SIMILAR TO USING '/'

#  first part is calling the function in our views second part is what is going in our template which needs to be in a template folder and this object 'artists' will render

urlpatterns = [
# artist and song index url paths
    path('', views.artist_list, name='artist_list'),
    path('songs/', views.song_list, name='song_list'),
# artist and song SHOW routes
    path('artists/<int:pk>', views.artist_detail, name='artist_detail'),
    path('songs/<int:id>', views.song_detail, name='song_detail'),
# artist and song CREATE routes
    path('artists/new', views.artist_create, name='artist_create'),
    path('songs/new', views.song_create, name='song_create'),
# artist and song EDIT routes
    path('artists/<int:pk>/edit', views.artist_edit, name='artist_edit'),
    path('songs/<int:id>/edit', views.song_edit, name='song_edit'),
# artist and song DELETE routes
    path('artists/<int:pk>/delete', views.artist_delete, name='artist_delete'),
  path('songs/<int:id>/delete', views.song_delete, name='song_delete'),
]
