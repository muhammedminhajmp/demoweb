from django.db import models

# Create your models here.
class dress(models.Model):
    name=models.CharField(max_length=230)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name



