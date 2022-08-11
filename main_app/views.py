from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import  Reading, Badge
from .forms import BookMarkForm
# Define the home view

def home(request):
  return render( request, 'home.html')
def about(request):
    return render( request, 'about.html')

def readings_index(request):
  readings = Reading.objects.all()
  return render(request, 'readings/index.html', { 'readings': readings })

def readings_detail(request, reading_id):
  reading = Reading.objects.get(id=reading_id)
  bookmark_form = BookMarkForm()
  return render(request, 'readings/detail.html', {
    'reading': reading, 'bookmark_form': bookmark_form
    })

class ReadingCreate(CreateView):
  model = Reading
  fields = '__all__'

class ReadingUpdate(UpdateView):
  model = Reading
  fields = ['genre', 'description', 'author']

class ReadingDelete(DeleteView):
  model = Reading
  success_url = '/readings/'

def add_bookmark(request, reading_id):
  form = BookMarkForm(request.POST)
  if form.is_valid():
    new_bookmark = form.save(commit=False)
    new_bookmark.reading_id = reading_id
    new_bookmark.save()
  return redirect('detail', reading_id=reading_id)

class BadgeList(ListView):
  model = Badge

class BadgeDetail(DetailView):
  model = Badge

class BadgeCreate(CreateView):
  model = Badge
  fields = "__all__"

class BadgeUpdate(UpdateView):
  model = Badge
  fields = "__all__"

class BadgeDelete(DeleteView):
  model = Badge
  success_url = '/badges/'