from django.db import models
from django.contrib.auth.models import User
from category.models import user_type, User_category
from django.db.models.signals import pre_save
from columbus.custom_lib import unique_id_generator, unique_otp_generator

class user_register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_code = models.CharField(max_length=500, null=True, blank=True)
    otp = models.IntegerField(null=True, blank=True)
    phone = models.BigIntegerField()
    join_as = models.ManyToManyField(user_type, verbose_name="join_as")
    category = models.ForeignKey(
        User_category, verbose_name="type", on_delete=models.CASCADE)
    discount_min = models.IntegerField()
    discount_max = models.IntegerField()

    def __str__(self):
        return str(self.user)

# function for unique code
def pre_save_create_user_id(sender, instance, *args, **kwargs):
    if not instance.user_code:
        instance.user_code = unique_id_generator(instance)
pre_save.connect(pre_save_create_user_id, sender=user_register)

# funtion for otp
def pre_save_create_otp(sender, instance, *args, **kwargs):
    if not instance.otp:
        instance.otp = unique_otp_generator(instance)
pre_save.connect(pre_save_create_otp, sender=user_register)