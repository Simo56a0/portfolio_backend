from django.shortcuts import render
from .models import Project, Post

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio_site/index.html', {'projects': projects})


def about(request):
    return render(request, 'portfolio_site/about.html')

def contact(request):
    return render(request, 'portfolio_site/contact.html')
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 6)  # Show 6 posts per page
    
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    
    return render(request, 'portfolio_site/blog.html', {'posts': posts})
def generic(request):
    return render(request, 'portfolio_site/generic.html')
def services(request):
    return render(request, 'portfolio_site/services.html')
def single(request):
    return render(request, 'portfolio_site/single.html')
def styles(request):
    return render(request, 'portfolio_site/styles.html')