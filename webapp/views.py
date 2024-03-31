from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import NameForm

# Create your views here.

def app(request):
    return HttpResponse("Hello this is django app example")

def template(request):

    index_template = loader.get_template('index.html')

    render_template = index_template.render({
        "name": "abdelali"
    })
    return HttpResponse(render_template)

def login(request):
    if request.method == 'GET':
        if 'firstname' in request.session:
            #del request.session['firstname']
            return render(request, 'success.html/', 
                          {"name": request.session['firstname'] if 'firstname' in request.session else ''})
        else:
            response = HttpResponse(render(request, 'form.html'))
            response.set_cookie(key="name", value="abdelali")
            return response

    elif request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            request.session['firstname'] = request.POST.get('firstname', '')
            return render(request, 'success.html/', {"name": request.POST.get('firstname', '')})

