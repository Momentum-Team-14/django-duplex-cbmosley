from django.contrib.auth.models import AbstractUser as BaseUser
from django.db import models

# Create your models here.


class User(BaseUser):
    # could add custom user attributes here
    pass

# model to make one snippet


class Snippet(models.Model):
    code = models.TextField()
    description = models.CharField(max_length=512, default="")
    language = models.ForeignKey(
        'Language', on_delete=models.CASCADE, related_name="snippets", blank=True, null=True)
    # related name should be the plural of the model that it's in. This a O2M rleationship. A snippet has one user. A user has many snippets.
    # user = models.ForeignKey(
    # User, on_delete=models.CASCADE, related_name="snippets")
    user = models.ManyToManyField(
        'User', related_name='snippets', )
    author = models.ForeignKey(
        'Author', on_delete=models.CASCADE, related_name="snippets")
    # if I wanted M2M
    # users = models.ManyToManyField('User', related_name='snippets')
    # if built snippet then take snippet descrition and language to be listed in description

    def __str__(self):
        return f'{self.description} in {self.language}'


class Language(models.Model):
    name = models.CharField(max_length=255)
    version = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.version}'
