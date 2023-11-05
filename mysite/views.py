from django.shortcuts import render, get_object_or_404
from mysite.models import Post, Episode
from datetime import datetime
from django.shortcuts import redirect
from .filters import BookFilter
from django.http import HttpResponseRedirect

# Create your views here.
def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session["is_dark_theme"] = not request.session.get('is_dark_theme')
    else:
        request.session["is_dark_theme"] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', {'posts': posts})

def intro(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    episodes = Episode.objects.filter(post=post)
    return render(request, 'intro.html', {'post': post, 'episodes': episodes})

def showepisode(request, episode_id):
    episode = get_object_or_404(Episode, id=episode_id)
    return render(request, 'post.html', {'episode': episode})

def filter(request):
    book = Post.objects.all()
 
    bookFilter = BookFilter(queryset=book)
 
    if request.method == "POST":
        bookFilter = BookFilter(request.POST, queryset=book)
 
    context = {
        'bookFilter': bookFilter
    }
 
    return render(request, 'filter.html', context)    

'''
def homepage(request):
    posts = Post.objects.all() #select * from post
    post_lists = list()
    for counter, post in enumerate(posts):
        post_lists.append(f'No. {counter}-{post} <br>')
    return HttpResponse(post_lists)
'''