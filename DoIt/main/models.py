from django.db import models
from django.contrib.auth.models import User

class Grouping(models.Model):
    title = models.CharField(max_length=50)
    done = models.BooleanField(default = False)
    created_on = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, models.CASCADE , related_name = "groupings")

    def __str__(self):
        return self.title

class Entry(models.Model):
    image = models.ImageField(upload_to = "media/images/entries" , blank = True)
    title = models.CharField(max_length=50 , default = "title_less")
    content = models.TextField()
    grouping = models.ForeignKey(Grouping , models.CASCADE , related_name = "entries")
    done = models.BooleanField(default = False)
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now = True)
    public = models.BooleanField(default = False)

    def __str__(self):
        return self.title
    



