from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,DetailView
from .forms import UserCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import mainContent,Subject,Grade,Topic
# Create your views here.



class SignUpCreateView(CreateView):

	form_class = UserCreateForm
	success_url = reverse_lazy('success')
	template_name = 'webapp/signup.html'


class SuccessView(TemplateView):
	template_name = 'webapp/success.html'




class HomeView( LoginRequiredMixin,ListView):
	login_url='/login/'
	template_name = 'webapp/index.html'

	def get_queryset(self):
		return Grade.objects.all()


class HomeDetailView(DetailView):
	model = Topic
	template_name='webapp/details.html'