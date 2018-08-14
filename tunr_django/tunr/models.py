from django.db import models
# EVERYTIME WE MAKE A CHANGE IN MODELS YOU HAVE TO:
# 1. MAKEMIGRATE
# 2. MIGRATE

# THIS SETS UP A NEW SCHEMA
# AND THEN MAKES A NEW TABLE IN SQL FOR US

# Create your models here.

# we are defining 3 fields (columns in our db) they are character fields which means we must add an upper limit to how many characters are in that db field
# we are giving photo_url unlimited length

# like a schema
class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    photo_url = models.TextField()

    # this is common for debugging
    def __str__(self):
        return self.name

# Foreign Keys
# Let's also start filling out the Song model. We will define the class and then add a foreign key. We do so like this:

# this is a child of artist
class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    preview_url = models.TextField()

    def __str__(self):
        return self.title
