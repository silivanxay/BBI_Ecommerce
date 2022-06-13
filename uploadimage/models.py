from django.db import models

class Image(models.Model):
    image = models.ImageField(blank=False, null=False)
    def __str__(self):
        return self.image.name