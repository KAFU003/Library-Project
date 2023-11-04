from django.shortcuts import render
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

def showintro(request, slug):
    try:
        post = Post.objects.get(slug=slug) 
        if post is not None:  # 使用 is not None 替代 !=
            return render(request, 'intro.html', {'post': post})  # 传递单个 post 变量      
        else:
            return redirect("/")    
    except:
        return redirect("/")

def showepisode(request, episode):
    # 获取特定书籍（Post 对象），如果不存在则返回 404 错误页面
    book = get_object_or_404(Post, pk=book_id)
    
    # 获取与该书籍关联的章节（Episode 对象）
    episodes = Episode.objects.filter(post=book)

    return render(request, 'intro.html', {'book': book, 'episodes': episodes})# 使用正确的变量名 book 和 episodes

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