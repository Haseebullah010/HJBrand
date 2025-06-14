from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import SubscribeForm

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Thank you for subscribing!'})
            messages.success(request, 'Thank you for subscribing!')
            return redirect('home')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            messages.error(request, 'Please correct the error below.')
    else:
        form = SubscribeForm()
    
    return render(request, 'index.html', {'form': form})
