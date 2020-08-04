from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Skill(models.Model):
    skill_name = models.CharField(max_length=100, null=True) 
    def __str__(self):
        return self.skill_name
        
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True,blank=True)
    phone = models.CharField(max_length=100, null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    bio = models.TextField(null=True,blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True,default='None')
    image = models.ImageField(upload_to='profile_img/', null=True,blank=True, default='avatar.png') 
    skills = models.ManyToManyField(Skill, null=True,blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            user=instance,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email,
        )
    



