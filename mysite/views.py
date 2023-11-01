from django.shortcuts import render
from mysite.models import Post
from datetime import datetime
from django.shortcuts import redirect
from .filters import BookFilter

# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())
    
def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug) 
        if post != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")    
    except:
        return redirect("/")
    #select * from post where slug=%slug

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