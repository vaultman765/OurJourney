from django.db import models


# Create your models here.
class Adventures(models.Model):
    OUTDOORS = 'OU'
    INDOORS = 'IN'
    TRIP = 'TR'
    OTHER = 'OT'
    CATEGORY_CHOICES = [
        (OUTDOORS, 'OUTDOORS'),
        (INDOORS, 'INDOORS'),
        (TRIP, 'TRIP'),
        (OTHER, 'OTHER')
    ]

    EXERCISE = 'EX'
    RELAX = 'RE'
    ROMANTIC = 'RO'
    FUN = 'FU'
    OTHER = 'OT'
    SUB_CATEGORY_CHOICES = [
        (EXERCISE, 'EXERCISE'),
        (RELAX, 'RELAX'),
        (ROMANTIC, 'ROMANTIC'),
        (FUN, 'FUN'),
        (OTHER, 'OTHER')
    ]

    adventure = models.CharField(max_length=500)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=OTHER)
    subcategory = models.CharField(max_length=2, choices=SUB_CATEGORY_CHOICES, default=OTHER)
    location = models.CharField(max_length=20)
    time = models.FloatField(default="")
    website = models.CharField(max_length=500, default="NA")
    details = models.TextField(max_length=2000, default="")
    image = models.ImageField(upload_to='images/', default='images/none/no_image.png')

    def __str__(self):
        return self.adventure
