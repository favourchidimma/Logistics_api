from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model
import random
from django.utils import timezone
from .models import*
import requests


def generate_otp():

    otp = random.randint(000000, 999999)
    return otp



User = get_user_model()

@receiver(post_save, sender=User)
def send_welcome_mail(sender, instance,created,**kwargs):

    if created:

        if instance.role in ('app_admin', 'root_admin', 'user'):

            instance.is_active = True

            instance.save()

            otp = generate_otp()
            print(otp)

            expiry_date = timezone.now() + timezone.timedelta(minutes=1)

            OTP.objects.create(
                otp = otp,
                expiry_date = expiry_date,
                user = instance

            )

        url = "https://api.useplunk.com/v1/track"
        header = {
            "Authorization": "Bearer sk_aa6b839adaff584665f2534d96a4f988ebe614d22767a1cd",
            "Content-Type": "application/json"
        }

        data = {
            "email": instance.email,
            "event": "signup",
            "data": {
                "full_name": instance.full_name,
                "otp": str(otp)
            }
        }

        response = requests.post(
            url=url,
            headers=header,
            json=data
        )

        print(response.json())






