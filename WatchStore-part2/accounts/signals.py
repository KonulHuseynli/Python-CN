from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import Profile
"""
post_save - Gonderen modelin save olunmasi zamani cagirir
pre_save - Gonderen model save olunmamisdan once cagrilir

post_delete - Gonderen modelin obyekti silindikden  sonra cagirir
pre_delete - Gonderen modelin obyekti silinmemisden evvel  cagrilir

post_migrate - Gonderen modelin miqrasiyasin zamani cagrilir
"""
@receiver(post_save, sender=User)#gonderen modelin obyekti save olunanda funksiyani ise salacaq
def create_profile(sender, instance, created, **kwargs):
    if created:
        # print(sender)#<class 'django.contrib.auth.models.User'>
        # print(instance) #Gonderen modelin{User}obyekti{user5(sonuncu yaratdigim user)}
        # print(created) #True
        # print(instance.password) #hash olunmus passwordu verir(sifreye birbasa catmaq olmaz)
        Profile.objects.create(user=instance)