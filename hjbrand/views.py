from django.shortcuts import render
from subscriptions.forms import SubscribeForm

def index(request):
    form = SubscribeForm()
    return render(request, 'index.html', {'form': form})
