from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404

def post_list(request):
    posts = Post.objects.all()
    
    
    context={
        "posts":posts
    }
    return render(request,"Blog/post_list.html",context)
# Create your views here.
def post_detail(request,pk):
     post=get_object_or_404(Post,pk=pk)
     context={
         "post":post
     }
     return render(request,"Blog/post_detail.html",context)
     