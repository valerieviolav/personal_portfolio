from django.db import models
import os 

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="project_images/", blank=True)
    def __str__(self):
        return self.title

class Training(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FileField(upload_to="training_images/", blank=True)
    file = models.FileField(upload_to="training_files/", blank=True)
    def __str__(self):
        return self.title
    def filename(self):
        return os.path.basename(self.file.name)
