from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from requests import auth


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.EmailField()
    avatar = models.ImageField(upload_to='avatars', blank=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
