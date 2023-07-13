from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

#def homepage(request):
    #return render(request, 'homepage.html')

class Homepage(ListView):
    model = Post 
    template_name = 'homepage.html'

class Submit_post(CreateView):
    model = Post
    template_name = "submit_post.html"
    fields = '__all__'
