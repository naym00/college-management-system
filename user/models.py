from help.choices import generic as CHOICE
from help.common.a_one import One as HELP
from django.contrib.auth.models import AbstractUser
from django.db import models

def uploadphoto(instance, filename):
    return "photo/{username}/all/{uniqueCode}-unique-{filename}".format(
        username=instance.username,
        uniqueCode=HELP().uniqueCode(),
        filename=filename
    )

class Usertype(models.Model):
    title = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f'{self.title}'
    
class User(AbstractUser):
    nickname = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=15, choices=CHOICE.GENDER, default=CHOICE.GENDER[0][1], blank=True, null=True)
    homedistrict = models.CharField(max_length=20, choices=CHOICE.DISTRICTS, blank=True, null=True)
    permanentaddress = models.TextField(blank=True, null=True)
    currentdistrict = models.CharField(max_length=20, choices=CHOICE.DISTRICTS, blank=True, null=True)
    presentaddress = models.TextField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    type = models.ForeignKey(Usertype, on_delete=models.SET_NULL, blank=True, null=True)
    phone = models.CharField(max_length=15, unique=True, blank=True, null=True)
    draft = models.BooleanField(default=False)

    def getfullname(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else f'{self.first_name}' if self.first_name else f'{self.last_name}'

class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to=uploadphoto, blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.username} - {self.title}'
    
class Profilepic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username}'
    
class Coverphoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username}'