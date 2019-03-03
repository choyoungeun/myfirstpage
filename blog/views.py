from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from django.core.paginator import Paginator
from django.utils import timezone

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all().order_by('-id')
    #모든 글들을 대상으로(객체는 최신순으로 정렬)
    paginator = Paginator(blog_list,3)
    #블로그 객체 3개를 한 페이지로 자르기
    page = request.GET.get('page')
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담는다)
    posts = paginator.get_page(page)
    #request된 페이지를 얻어온 뒤 return해 준다.
    return render(request,'home.html',{'blogs':blogs, 'posts':posts})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def contact(request):
    return render(request,'contact.html')

