from django.db import models

class Image(models.Model):
    image = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.image.name