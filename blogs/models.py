"""
1. We do migration so that this class/model (which is an instance of the database table),
is mapped to a db table. -- basically django doesnt know that this class = some table
2. CREATE a Migration file - tracks any changes that we make in any model. -- by running makemigrations
3. ORM bridges gap between code and the database. We can do things like save instance of model,
retrieve model from db etc.

"""

from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  # automatically populate date with this bool value
    thumbnail = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')],
                              default='published')

    def __str__(self):
        return self.title

    def shorter_body(self):
        return self.body[:70] + "..."


class Member(User):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    province = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def number_of_blogs_posted(self):
        return Blog.objects.filter(author=self, status='published').count()


# Model for Comments on Blogs
class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


# Model for Likes on Blogs
class Like(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f"{self.user} likes {self.post}"


# Model for Events around you for green initiatives
class Event(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
