
from django.shortcuts import render

from recordapi.models import Fish

def index(request):
    context = {
        'fishes': Fish.objects.all(),
    }
    return render(request, 'fish/fish_list.html', context)
