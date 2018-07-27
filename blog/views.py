from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import publication, Comments
from django.urls import reverse
from datetime import datetime


# Create your views here.
def blog_new(request):
    if request.method == "POST":
        form_post = PostForm(request.POST)
        if form_post.is_valid():
            post = form_post.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('blog:blog_view', args=[3]))
    else:
        form_post = PostForm()
    return render(request, 'blog/create_blog.html', {'form_post': form_post})

@login_required
def blog_edit(request, pk):
    post = get_object_or_404(publication, pk=pk)
    not_this_user = get_object_or_404(publication, id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = datetime.now()
            post.save()
            return redirect('blog:full_blog', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/blog_edit.html', {'form': form, 'not_this_user': not_this_user})

def blog_list(request, pk):
    blogs_list = publication.objects.all()
    if pk == 1:
        blogs_list = blogs_list.order_by('-author')
    elif pk == 2:
        blogs_list = blogs_list.order_by('-pub_date')
    return render(request, 'blog/all_blogs.html', {'blogs_list': blogs_list,
                                                   # 'sort_by_author': sort_by_author,
                                                   # 'sort_by_pub_date': sort_by_pub_date
                                                   },)

def blog_detail(request, pk):
    full_blog = get_object_or_404(publication, id=pk)
    comment = Comments.objects.filter(new=pk)
    if request.method == "POST":
        form_for_comment = CommentForm(request.POST)
        if form_for_comment.is_valid():
            form = form_for_comment.save(commit=False)
            form.user = request.user
            form.new = full_blog
            form.save()
            return redirect('blog:full_blog', pk=full_blog.pk)
    else:
        form_for_comment = CommentForm()
    return render(request, 'blog/full_blog.html',
                  {'full_blog': full_blog,
                  'comments': comment,
                  'form_for_comment': form_for_comment})

def blog_remove(request, pk):
    post = get_object_or_404(publication, pk=pk)
    post.delete()
    return HttpResponseRedirect(reverse('blog:blog_view', args=[3]))