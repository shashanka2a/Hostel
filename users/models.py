from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # roll_no = models.CharField(max_length=255,blank=True,null=True,unique=True)
    full_name = models.CharField(max_length=255,blank=True,null=True)
    phone = models.IntegerField(blank=True,null=True)
    parent_phone = models.IntegerField(blank=True,null=True)
    #photo = models.ImageField(blank=True,null=True)
    gender = models.CharField(max_length=255,blank=True,null=True)
    role = models.CharField(max_length=255,blank=True,null=True)


    def __str__(self):
        return self.username


class Request(models.Model):
    from_user = models.ForeignKey(CustomUser,on_delete=None,related_name='from_user')
    assigned_to = models.ForeignKey(CustomUser,on_delete=None,related_name='assigned_to')
    when = models.DateField(blank=True,null=True)
    return_date  = models.DateField(blank=True,null=True)
    place = models.CharField(max_length=255,blank=True,null=True)
    purpose = models.CharField(max_length=255,blank=True,null=True)

class Partners(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=None,related_name='user')
    when = models.DateField(blank=True,null=True)
    return_date  = models.DateField(blank=True,null=True)
    place = models.CharField(max_length=255,blank=True,null=True)
    purpose = models.CharField(max_length=255,blank=True,null=True)

