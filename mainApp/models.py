from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
# Create your models here.


class Tags(models.Model):
    tag_name = models.CharField(max_length=40)
    tag_user = models.ForeignKey(User,on_delete=models.CASCADE,)
    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse('tag-update', kwargs={'pk': self.id})

    class Meta:

        ordering = ('tag_name',)

class Events(models.Model):
    event_name = models.CharField(max_length=40)
    event_user = models.ForeignKey(User,on_delete=models.CASCADE,)
    def __str__(self):
        return self.event_name
    def get_absolute_url(self):
        return reverse('evemt-update', kwargs={'pk': self.id})
        1
    class Meta:

        ordering = ('event_name',)

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
    US = 'USA'
    CANADA = 'CAN'
    SAMERICA = 'SAM'
    UK = 'UNK'
    FRANCE= 'FRA'
    ASIA= 'ASN'
    OTHEREURO = 'OEU'
    OTHER = 'OTH'
    COUNTRY_CHOICES = (
        (US, 'United States'),
        (CANADA, 'Canada'),
        (UK, 'United Kingdom'),
        (SAMERICA, 'South America'),
        (FRANCE, 'France'),
        (ASIA, 'Asia'),
        (OTHEREURO, 'Europe'),
        (OTHER, 'Other'),
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
    country = models.CharField(
        max_length=3,
        choices = COUNTRY_CHOICES,
        blank = True,
        default=US
        )
    twitter = models.URLField(blank = True,)
    youtube = models.URLField(blank = True,)
    twitch = models.URLField(blank = True,)
    notes = models.TextField(blank = True,)
    tags = models.ManyToManyField(Tags,blank=True)
    events = models.ManyToManyField(Events,blank=True)

    def __str__(self):
        return self.influencer_name

    def get_absolute_url(self):
        return reverse('influencer-update', kwargs={'pk': self.id})

    class Meta:

        ordering = ('influencer_name',)

class List(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,)
    list_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list_name = models.CharField(max_length=50)
    influencers = models.ManyToManyField(Influencer,blank=True)

    def __str__(self):
        return self.list_name

    def get_absolute_url(self):
        return reverse('list-update', kwargs={'pk': self.list_id})
