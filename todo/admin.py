from django.contrib import admin
from todo.models import (Number, Item, Priority, Depedency)

for x in [Number, Item, Priority, Depedency]:
    admin.site.register(x)
