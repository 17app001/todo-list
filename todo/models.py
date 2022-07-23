from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# title -str
# text  -str (blank=True)
# created  -datetime  -(auto=True)
# date_completed -datetime - (blank=True,null=True)
# important -bool - (default=False)
# completed -bool - (default=False)


class Todo(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=True)
    completed = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} -{self.title}-{self.created}-({self.user.username})'
