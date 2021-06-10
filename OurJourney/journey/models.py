from django.db import models


# Create your models here.
class Adventures(models.Model):
    adventure = models.CharField(max_length=500)
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    website = models.CharField(max_length=500, default="NA")
    image = models.ImageField(upload_to='images/', default='images/none/no_image.png')

    def __str__(self):
        return self.adventure
