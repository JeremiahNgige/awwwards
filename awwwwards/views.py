from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
import random

# Create your views here.
def index(request):
    try:
        posts=Post.objects.all()
        posts = posts[::-1]
        one_post = random.randint(0, len(posts)-1)
        random_post = posts[one_post]
        print(random_post)
    except:
        posts = None
    return render(request, 'awwwwards/index.html', locals())

class PostListView(ListView):
    model = Post
    template_name = 'awwwwards/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'description', 'image_url', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)