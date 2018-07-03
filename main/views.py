from django.shortcuts import render
from django.http import HttpResponse
from .models import Pais

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    from IPython import embed; embed()

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})
