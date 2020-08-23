from django.db import models
from django.contrib.auth.models import User
# from autoslug import AutoSlugField

class city(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return str(self.city)

class dest_detail(models.Model):
    title = models.CharField(max_length=50)
    # slug = AutoSlugField(populate_from='title', null=True, blank=True)
    city = models.ForeignKey(
        city, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_by")

    address = models.TextField(null=True, blank=True)
    cover_photo = models.ImageField(
        upload_to='destination_cover_photo', null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    how_to_reach = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name="created_by")

    def __str__(self):
        return str(self.title)

class dest_video(models.Model):
    dest_detail = models.ForeignKey(
        dest_detail, on_delete=models.CASCADE)
    video = models.FileField(
        upload_to='destination_video', null=True, blank=True)

def __str__(self):
    return str(self.video)

class dest_photo(models.Model):
    dest_detail = models.ForeignKey(
        dest_detail, on_delete=models.CASCADE)
    photo_name = models.CharField(max_length=50, null=True, blank=True)
    photos = models.ImageField(upload_to='destionation_photos', height_field=None,
                               width_field=None, max_length=None, null=True, blank=True)

def __str__(self):
    return str(self.photo_name)