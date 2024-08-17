from django.shortcuts import render, redirect, get_object_or_404
from blog.models import PostModel
from .forms import PostForm



# Create your views here.

def post_list(request):
    posts = PostModel.objects.all().order_by("-created_at")
    context = {
        "posts": posts,
    }
    return render(request, "blog/post_list.html", context)
 

def post_detail(request, pk):
    post = PostModel.objects.get(pk=pk)
    context = {
        "post": post
    }
    return render(request, "blog/post_detail.html", context)
   

def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        else:
            return render(request, "blog/create_post.html", {'form': form})
    return render(request, "blog/create_post.html", {'form': form})    
   
             
            
 
        
        
    
  

# def post_edit(request, pk):
#     post = get_object_or_404(PostModel, pk)
#     form = PostForm(intance=post)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid:
#             form.save()
#             return redirect('post_detail', pk=pk)
#         else:
#              return render(request, "blog/create_post.html", {'form': form})
        
#     return render(request, "blog/create_post.html", {'form': form})
    
   
      
    

def post_delete(request, id):
    post = get_object_or_404(PostModel,id=id)
    post.delete()
    return redirect('post_list')
    
   
