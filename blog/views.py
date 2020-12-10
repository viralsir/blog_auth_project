from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from .models import Post
# Create your views here.
# app/model_form.html
# blog/Post_form.html
# blog/Post_list.html

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content','author']

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    ordering = ['-date_posted']


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content','author']

class PostDetailView(DetailView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/post/view/'

    def test_func(self):
        post=self.get_object()
        if post.author == self.request.user :
            return True
        else:
            return False


#blog/Post_detail.html
#blog/Post_confirm_delete.html