from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

class Authors(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=50, null=False)
    born_location = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=5000, null=False)

    def __str__(self):
        return self.fullname

class Qoutes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    quote = models.CharField(max_length=5000, null=False)