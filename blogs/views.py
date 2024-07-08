from django.shortcuts import render, redirect
from .models import Blog
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


def blogs_list(request):
    blogs = Blog.objects.all().order_by('pub_date')
    return render(request, 'blogs/blogs_list.html', {'blog_details': blogs})


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blogs/blog_detail.html', {'blog': blog})


@login_required(login_url="/accounts/login/")  # Redirect if user not logged-in
def blog_create(request):
    if request.method == 'POST':
        # request.files as .POST does not include attached files data! :(
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            # Save blog to the database
            blog_instance = form.save(commit=False)
            blog_instance.author = request.user
            blog_instance.save()
            return redirect('blogs:blogs_list')
    else:
        form = forms.CreateBlog()
    return render(request, 'blogs/blog_create.html', {'form_UI': form})
