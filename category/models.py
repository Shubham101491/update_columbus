from django.db import models

class user_type(models.Model):
    type = models.CharField(max_length=50)
    publish_status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.type)

class User_category(models.Model):
    type = models.CharField(max_length=50)
    publish_status = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.type)