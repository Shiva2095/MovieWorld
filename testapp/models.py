from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Movie(models.Model):
    rdate = models.DateField()
    movien = models.CharField(max_length=255)
    hero = models.CharField(max_length=255)
    heroin = models.CharField(max_length=255)
    rating = models.IntegerField(default=1,
        validators=[MaxValueValidator(10), MinValueValidator(1)])

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
