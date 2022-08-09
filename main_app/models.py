from django.urls import reverse
from django.db import models

# readings = [
#   reading('ULYSSES', 'Modernist novel', 'Ulysses is the story of a day in the life of Leopold Bloom as he travels Dublin and goes about his business, attending a funeral, buying soap, going to the Library, walking by the beach, going to the pub etc', 'James Joyce'),
#   reading('THE GREAT GATSBY', 'Tragedy, Realism, Modernism,', 'the tragic story of Jay Gatsby, a self-made millionaire, and his pursuit of Daisy Buchanan, a wealthy young woman whom he loved in his youth.', 'F. Scott Fitzgerald'),
#   reading('LOLITA', 'Novel', 'In Lolita, a middle-aged man named Humbert Humbert becomes obsessed with a pre-pubescent girl named Dolores Haze, who he calls Lolita. ', 'Vladimir Nabokov')
# ]

class Reading(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'reading_id': self.id})