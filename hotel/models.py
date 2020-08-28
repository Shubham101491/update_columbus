from django.db import models

class hotels_data(models.Model):
    hotel_name = models.CharField(max_length=50)
    destination = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    zipcode = models.IntegerField()
    about_hotel = models.CharField(max_length=500)
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    linkdin = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    google_user = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

    def __str__(self): 
        return self.hotel_name