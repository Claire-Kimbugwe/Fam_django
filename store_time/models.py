from django.db import models


# I am using SQLite3  because it's quick 
# and easy, but it's not an appropriate database if you were 
# to launch your app — it was built to support only a single user at a time



# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)