from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.TextField()
    audio_file = models.FileField(blank=True,null=True)
    paginate_by = 2

    def __str__(self):
        return self.title
# Create your models here.

class backsong(models.Model):
    title=models.TextField()
    audio=models.FileField(blank=True,null=True)

    def __str__(self):
        return self.title
