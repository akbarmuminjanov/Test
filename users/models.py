from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images/", default="default.png/jpg")
    bio = models.CharField(max_length=150, blank=True, null=True)
    close_acc = models.BooleanField(default=False)

    def __str__(self):
        return str(f"Profile of {str(self.user.first_name)}")
    
