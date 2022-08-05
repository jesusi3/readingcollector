from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
class reading:  # Note that parens are optional if not inheriting from another class
  def __init__(self, title, genre,  description, author):
    self.title = title
    self.genre = genre
    self.description = description
    self.author = author

readings = [
  reading('ULYSSES', 'Modernist novel', 'Ulysses is the story of a day in the life of Leopold Bloom as he travels Dublin and goes about his business, attending a funeral, buying soap, going to the Library, walking by the beach, going to the pub etc', 'James Joyce'),
  reading('THE GREAT GATSBY', 'Tragedy, Realism, Modernism,', 'the tragic story of Jay Gatsby, a self-made millionaire, and his pursuit of Daisy Buchanan, a wealthy young woman whom he loved in his youth.', 'F. Scott Fitzgerald'),
  reading('LOLITA', 'Novel', 'In Lolita, a middle-aged man named Humbert Humbert becomes obsessed with a pre-pubescent girl named Dolores Haze, who he calls Lolita. ', 'Vladimir Nabokov')
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render( request, 'about.html')

def readings_index(request):
    return render(request, 'readings/index.html', { 
        'readings': readings 
        })