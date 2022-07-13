from django.shortcuts import render
from .models import Post
from django.utils import timezone
def post_list(request):
    posts = Post.objects.all()
    
    
    context={
        "posts":posts
    }
    return render(request,"Blog/post_list.html",context)
# Create your views here.
