from django.db import models
from django.contrib.auth.models import User


class Number(models.Model):  # Phone Number
    number = models.CharField(max_length=32, unique=True)
    who = models.ForeignKey(User, related_name='numbers')


class Priority(models.Model):
    name = models.CharField(max_length=16)
    description = models.TextField()
    weight = models.IntegerField()
    critical = models.BooleanField(default=False)


class Item(models.Model):
    who = models.ForeignKey(User, related_name='agenda_items')
    created_at = models.DateTimeField(auto_now=True)
    finished = models.BooleanField(default=False)
    finished_at = models.DateTimeField(null=True)
    due_date = models.DateTimeField(null=True)
    description = models.TextField()
    priority = models.ForeignKey(Priority, related_name='items')


class Depedency(models.Model):
    blocked_job = models.ForeignKey(Item, related_name='blocked_by')
    blocking_job = models.ForeignKey(Item, related_name='blocking')
