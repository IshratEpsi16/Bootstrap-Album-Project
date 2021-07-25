from django.db import models

# Create your models here.
class album_db(models.Model):
    image = models.ImageField(upload_to='album/photo/')
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.description
    
