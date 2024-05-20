from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Subscriber
from .forms import SubscriberForm

def index(request):
    posts = Post.objects.all()
    form = SubscriberForm()
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'posts': posts, 'form': form}
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
