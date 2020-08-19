import random
import string
# from django.utils.text import slugify

# function for unique code
def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_id_generator(instance):
    order_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(user_code=order_new_id).exists()
    if qs_exists:
        return unique_id_generator(instance)
    return order_new_id

# funtion for otp
def random_string_otp_generator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_otp_generator(instance):
    order_new_otp = random_string_otp_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(user_code=order_new_otp).exists()
    if qs_exists:
        return unique_otp_generator(instance)
    return order_new_otp