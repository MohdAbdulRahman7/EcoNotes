"""
1. We do migration so that this class/model (which is an instance of the database table),
is mapped to a db table. -- basically django doesnt know that this class = some table
2. CREATE a Migration file - tracks any changes that we make in any model. -- by running makemigrations
3. ORM bridges gap between code and the database. We can do things like save instance of model,
retrieve model from db etc.

"""

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  # automatically populate date with this bool value
    thumbnail = models.ImageField(default='default.png', blank=True)

    def __str__(self):
        return self.title

    def shorter_body(self):
        return self.body[:70] + "..."
