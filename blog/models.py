from django.db import models

# Create your models here.
class FilesAdmin(models.Model):
    adminupload=models.FileField(upload_to='images')
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title