from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Reading
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
  return render(request, 'readings/detail.html', {'reading': reading})

class ReadingCreate(CreateView):
  model = Reading
  fields = '__all__'

class ReadingUpdate(UpdateView):
  model = Reading
  fields = ['genre', 'description', 'author']

class ReadingDelete(DeleteView):
  model = Reading
  success_url = '/readings/'