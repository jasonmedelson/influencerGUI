from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Tags(models.Model):
    tag_name = models.CharField(max_length=40)

class Events(models.Model):
    event_name = models.CharField(max_length=40)

class Influencer(models.Model):
    XSMALL = 'XS'
    SMALL = 'SM'
    MEDIUM = 'MD'
    LARGE = 'LG'
    XLARGE = 'XL'
    XXLARGE = '2X'
    XXXLARGE = '3X'
    XXXXLARGE = '4X'
    XXXXXLARGE = '5X'
    SHIRT_SIZE_CHOICES = (
        (XSMALL, 'X Small'),
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
        (XLARGE, 'X Large'),
        (XXLARGE, '2X Large'),
        (XXXLARGE, '3X Large'),
        (XXXXLARGE, '4X Large'),
        (XXXXXLARGE, '5X Large'),
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    influencer_name = models.CharField(max_length=50)
    email = models.EmailField(blank = True)
    mailing_address = models.TextField(blank = True)
    phone = models.CharField(max_length=20,blank = True)
    shirt = models.CharField(
        max_length=2,
        choices = SHIRT_SIZE_CHOICES,
        default = XLARGE,
        blank = True,
    )
    twitter = models.URLField(blank = True,)
    youtube = models.URLField(blank = True,)
    twitch = models.URLField(blank = True,)
    notes = models.TextField(blank = True,)
    tags = models.ManyToManyField(Tags)
    events = models.ManyToManyField(Events)

    def __str__(self):
        return self.influencer_name

    class Meta:

        ordering = ('influencer_name',)
