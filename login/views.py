from __future__ import absolute_import
from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse, reverse_lazy
from braces import views
from django.template import RequestContext

#relative imports
from .forms import RegistrationForm, LoginForm
#from talks.models import TalkList

class AccountView(generic.TemplateView, views.LoginRequiredMixin):
	template_name = "account.html"

class HomePageView(generic.TemplateView):
	template_name = 'home.html'

class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin,
                 generic.CreateView):
    form_class = RegistrationForm
    form_valid_message = "Thanks for signing up! Go ahead and login."
    model = User
    success_url = reverse_lazy('login:login')
    template_name = 'signup.html'
'''
Creates a list from previous app
    def form_valid(self, form):
        resp = super(SignUpView, self).form_valid(form)
        TalkList.objects.create(user=self.object, name='To Attend')
        return resp
'''
class LoginView(
	views.AnonymousRequiredMixin,
	views.FormValidMessageMixin,
	generic.FormView):
	form_class = LoginForm
	form_valid_message = "You're logged in now."
	template_name = 'login.html'

	def get_success_url(self):
		return reverse('login:home')

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.form_invalid(form)

class LogOutView(
	views.LoginRequiredMixin,
	views.MessageMixin,
	generic.RedirectView):
	def get_redirect_url(self):
		return reverse('login:login')

	def get(self, request, *args, **kwargs):
		logout(request)
		self.messages.success("You've been logged out. Come back soon!")
		return super(LogOutView, self).get(request, *args, **kwargs)

