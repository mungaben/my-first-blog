from django.shortcuts import render

def post_list(request):
    context={
        
    }
    return render(request,"Blog/post_list.html",context)
# Create your views here.
