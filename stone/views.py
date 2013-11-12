from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    request.session['active_page'] = 'home'
    active_page = request.session['active_page']
    is_login = False
    if request.user.is_authenticated():
        is_login = True

    return render(request, 'index.html',  {'active_page':active_page, 'is_login':is_login})