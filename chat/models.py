from PIL import Image
import requests
from io import BytesIO

from django.db import models

# Create your models here.


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.TextField()
    #profile_picture = models.ImageField(default=Image.open(BytesIO(requests.get('https://www.ienglishstatus.com/whatsapp-dp-images-profile-pictures/').content)))
    group = models.ManyToManyField(Group)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
