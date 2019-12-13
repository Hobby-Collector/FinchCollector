from django.shortcuts import render

from django.http import HttpResponse

class Finch:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Lolo', 'feathered', 'foul little demon', 3),
  Finch('Sachi', 'featherless', 'he hasn''t hatched yet so ya know', 0),
  Finch('Raven', 'not a finch', 'he is just a raven I didnt choose him he chose me', 4)
]

# Create your views here.
def home(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')

def finches_index(request):
    return render(request,'finches/index.html', {'finches': finches})