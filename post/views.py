from django.shortcuts import render,redirect
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'pos':posts})

def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'posts.html',{'pos':posts})

def post_create(request):
    return render(request, 'create_post.html')

def post_process(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        # Create a new post entry in the database using the Post model
        post = Post.objects.create(title=title, body=body)
        # or 
        # post = Post(title=title, body=body)
        post.save()
        return redirect('index')
    else:
        return render(request,'create_post.html')
