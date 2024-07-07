"""
We need to add here, so that we see our models/tables in the admin panel.
"""

from django.contrib import admin
from .models import Blog # From models.py file import Blog class

# Register your models here.
admin.site.register(Blog)


