from __future__ import unicode_literals
import bcrypt
import datetime
from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate_user(self, post):
        isValid = True
        if len(post.get('name')) < 3:
            isValid = False
        if len(post.get('username')) < 3:
            isValid = False
        if len(post.get('password')) < 8:
            isValid = False
        if post.get('password') != post.get('password2'):
            isValid = False
        return isValid

    def login_user(self, post):
        user = self.filter(username = post.get('username')).first()
        name = self.filter(name = post.get('name'))
        if user.password == bcrypt.hashpw(post['password'].encode(), user.password.encode()):
            return (True, user, name)
        return (False, 'notuser')

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=500)
    password = models.CharField(max_length=500)
    date_hired = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Wish_listManager(models.Manager):
    def validate_item(self, post):
        isValid = True
        if len(post.get('item')) < 3:
            isValid = False
        return isValid


class Wish_list(models.Model):
    item = models.CharField(max_length = 500)
    added_by = models.CharField(max_length = 255)
    date_added = models.DateField(auto_now=True)
    wishers = models.ManyToManyField(User)
    objects = Wish_listManager()
