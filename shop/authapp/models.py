from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


def default_key_expiration_date():
    return timezone.now() + timedelta(hours=48)


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)

    activation_key = models.CharField(verbose_name="Ключ активации", max_length=128, null=True)
    activation_expiration_date = models.DateTimeField(
        verbose_name="Активация истекает", default=default_key_expiration_date)

    def is_activation_key_expired(self):
        return self.activation_expiration_date < timezone.now()


class ShopUserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'W'
    NONBINARY = 'X'

    GENDER_CHOICES = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
        (NONBINARY, 'Небинарный')
    )

    user = models.OneToOneField(ShopUser, null=False, db_index=True, on_delete=models.CASCADE, related_name='profile')
    tagline = models.CharField(verbose_name='теги', max_length=128, blank=True)
    about_me = models.TextField(verbose_name='о себе', max_length=512, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)

    @receiver(post_save, sender=ShopUser)
    def create_or_save_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)
        else:
            instance.profile.save()

