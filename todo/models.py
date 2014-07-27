from django.db import models


class Number(models.Model):
    number
    who


class Item(models.Model):
    who
    created_at
    finished
    finished_at
    due_date
    description
    priority


class Priority(models.Model):
    description
    weight
    critical


class Depedency(models.Model):
    blocked_job  # Job that is blocked
    blocking_job  # Job that is blocking
