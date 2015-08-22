from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Member(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=120, blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    avatar = models.FileField(upload_to='media/images/', blank=True, null=True)
    timestamp=models.DateField(auto_now_add=True, auto_now=False)
    updated=models.DateField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('member_update', kwargs={'pk': self.pk})