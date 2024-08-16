from django.db import models
import uuid

# Create your models here.

class User(models.Model):
    class bg(models.TextChoices):
        not_available = "NOTA"
        o_positive = "o+"
        o_negative = "o-"
        ab_positive = "ab+"
        ab_negative = "ab-"
        a_positive = "a+"
        a_negative = "a-"
        b_positive = "b+"
        b_negative = "b-"

    username = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True,null=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age =  models.IntegerField()
    gender = models.CharField(max_length=20)
    # profilePicture = models.BinaryField(editable=True)
    permissionLevel = models.IntegerField()
    email = models.EmailField()
    userId = models.UUIDField(auto_created=True,editable=False,default=uuid.uuid4,null=False,unique=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    nickname = models.CharField(max_length=50)
    bio = models.TextField()
    bloodGroup = models.TextField(choices=bg)

    def __str__(self):
        return self.username