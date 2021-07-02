from django.db import models
from django.urls import reverse


# Create your models here.
class Adventures(models.Model):
    OUTDOORS = 'Outdoors'
    INDOORS = 'Indoors'
    TRIP = 'Trip'
    OTHER = 'Other'
    CATEGORY_CHOICES = [
        (OUTDOORS, 'OUTDOORS'),
        (INDOORS, 'INDOORS'),
        (TRIP, 'TRIP'),
        (OTHER, 'OTHER')
    ]

    EXERCISE = 'Exercise'
    RELAX = 'Relaxation'
    ROMANTIC = 'Romantic'
    FUN = 'Fun'
    OTHER = 'Other'
    SUB_CATEGORY_CHOICES = [
        (EXERCISE, 'EXERCISE'),
        (RELAX, 'RELAX'),
        (ROMANTIC, 'ROMANTIC'),
        (FUN, 'FUN'),
        (OTHER, 'OTHER')
    ]

    adventure = models.CharField(max_length=500)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default=OTHER)
    subcategory = models.CharField(max_length=10, choices=SUB_CATEGORY_CHOICES, default=OTHER)
    location = models.CharField(max_length=200)
    hours = models.FloatField(default='0.0')
    website = models.CharField(max_length=500, default="NA")
    details = models.TextField(max_length=2000, default="")
    image = models.ImageField(upload_to='adventures/planned/images/', default='adventures/planned/none/no_image.png')

    def __str__(self):
        return self.adventure

    def get_absolute_url(self):
        return reverse("journey:detail", kwargs={"id": self.id})


class TakenAdventures(models.Model):
    image = models.ImageField(upload_to='adventures/taken/images/', default='')
    caption = models.TextField(default="")
    location = models.CharField(default="", max_length=200)
    date = models.CharField(default="", max_length=200)

    def __str__(self):
        return self.caption