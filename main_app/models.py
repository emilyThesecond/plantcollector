from django.db import models
from django.urls import reverse

METHOD = (
    ('T', 'Top-Watering'),
    ('B', 'Bottom-Watering')
)

# Create your models here.
class Soil(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('soil_detail', kwargs={'pk': self.id})

class Plant(models.Model):
    name = models.CharField(max_length=100)
    common_name= models.CharField(max_length=100)
    family = models.TextField(max_length=250)
    soils = models.ManyToManyField(Soil)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})
    
class Watering(models.Model):
    date = models.DateField('Watering Date')
    method = models.CharField(
        max_length=1,
        choices = METHOD,
        default=METHOD[0][0]
        )
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_method_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']
    