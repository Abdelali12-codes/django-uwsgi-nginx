from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponse,HttpResponseServerError

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse(render(request, 'success.html', {'name': request.POST.get('firstname', '')}))
    
    return render(request, 'register.html', {'form': form })