from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic import TemplateView


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/home/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None

class HomeView(TemplateView):
    template_name = 'home.html'
