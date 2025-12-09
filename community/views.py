from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm


def community_home(request):
    posts = Post.objects.all()
    return render(request, 'community/index.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('community:home')
    else:
        form = PostForm()
    return render(request, 'community/create_post.html', {'form': form})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('created_at')

    # Логіка додавання коментаря
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('community:detail', pk=pk)
    else:
        comment_form = CommentForm()

    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'is_liked': is_liked,
        'total_likes': post.total_likes()
    }
    return render(request, 'community/post_detail.html', context)


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return redirect('community:detail', pk=pk)
