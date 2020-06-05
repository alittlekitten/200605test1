from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog
# Create your views here.

def home(request):
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})


def write(request):
    return render(request, 'write.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['boardtitle']
    blog.body = request.GET['boardbody']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/board/' + str(blog.id))


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog_detail})