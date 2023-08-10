from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    dp = models.ImageField(upload_to="images/dps/",default="images/dps/def.png")
    about = models.TextField(blank=True)
    bday = models.DateField(null=True,blank=True)
    created = models.DateField(auto_now_add = True)
    edited = models.DateField(auto_now=True)
    user = models.OneToOneField(User , models.CASCADE )


    gender_choices = (
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )

    gender = models.CharField(max_length=50 , choices = gender_choices , blank = True)

    def __str__(self):
        return self.user.username
    