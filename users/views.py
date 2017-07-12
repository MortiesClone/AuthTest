#from django.shortcuts import render
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
#from django.views.generic import TemplateView, ListView
#from django.core.context_processor import csrf

def login(request):
    args = {}
    args.update(request)
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")

#from django.views.generic import TemplateView, ListView

#class LoginView(TemplateView):
    #template_name = 'login.html'
