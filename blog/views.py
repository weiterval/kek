from django.shortcuts import render, redirect

from blog.forms import CommentForm
from blog.models import Post



def post_list(request):
    posts=Post.objects.all()
    return render(request, "blog/post_list.html", {"posts":posts})

def post_view(reguest,id):
    from blog.forms import CommentForm
    post=Post.objects.get(id=id)
    return render(reguest,"blog/post_view.html",{"post":post,"comment_form":CommentForm(initial={"post":post.id})})

def comment_form(reguest):
    com=CommentForm(reguest.POST)
    com.save()
    return redirect("/blog/post/"+str(com.instance.post_id))
