from django.db import models
from userprofile.models import User
class EllaManager(models.Manager):
    def get_queryset(self):
        return super(EllaManager,self).get_queryset().filter(is_active=True)

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=160)
    created_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    objects=models.Manager()
    ella_tweets=EllaManager()

    def __str__(self):
        return self.text
class HashTag(models.Model):
    name=models.CharField(max_length=64,unique=True)
    tweet=models.ManyToManyField(Tweet)

    def __str__(self):
        return self.name
# Create your models here.
