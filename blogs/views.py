from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse


def blogs_list(request):
    blogs = Blog.objects.all().order_by('pub_date')
    return render(request, 'blogs/blogs_list.html', {'blog_details': blogs})


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})

