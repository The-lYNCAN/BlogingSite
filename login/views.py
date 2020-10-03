from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, DetailView, FormView, CreateView, ListView, UpdateView
from django.urls import reverse
from django.views.generic import View
from django.views.generic.edit import FormMixin
from login.forms import signup_form, login_form
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from login import models
from login.forms import commenting
from django.contrib.auth.views import login_required
# Create your views here.
class Index_view(TemplateView):
    template_name = 'index.html'
    def post(self, request):
        if self.request.method == "POST":
            print("this time its a post")
            print(self.request.user)
            return HttpResponseRedirect(reverse('login:signup'))

class signup_view(FormView):
    template_name = 'signup.html'
    form_class = signup_form
    success_url = '/login/index'
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('login:index'))

class login_view(FormView):
    form_class = login_form
    template_name = 'login.html'
    success_url = '/login/index'
    def form_valid(self, form):
        name = self.request.POST.get('username')
        password = self.request.POST.get("password")
        print(self.request.POST)
        print(name)
        details = authenticate(self.request, username=name, password=password)
        print(name)
        if details:
            login(self.request, details)
            return HttpResponseRedirect(reverse('login:index'))
        else:
            return HttpResponse("wrong username")
class Blog_creation(CreateView):
    model = models.blog_model
    fields = [
        'title',
        'content',
    ]
    template_name = 'blog_creation.html'
    def get_success_url(self):
        return reverse('login:index')
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = str(self.request.user)
        self.object.save()
        return super(Blog_creation, self).form_valid(form)


class listing_blogs(ListView):
    template_name = 'blogs.html'
    model = models.blog_model

class complete_blog(FormMixin, DetailView):
    from login.models import blog_model
    template_name = 'detail.html'
    model = models.blog_model
    form_class = commenting
    def get_context_data(self, **kwargs):
        data = super(complete_blog, self).get_context_data(**kwargs)
        data['comments'] = models.comments.objects.all()
        data['form'] = self.get_form()
        return data
    def get_success_url(self):
        return reverse('login:blog_complete', kwargs={'pk':self.get_object().pk})

    def post(self, request, pk):
        print('its a post')
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = str(self.request.user)
        print(str(self.get_object().title))
        self.object.blog = str(self.get_object().title)
        self.object.save()
        return super(complete_blog, self).form_valid(form)

    #def form_valid(self, form):
     #   print("its a valid form")


class update_blog(UpdateView):
    model = models.blog_model
    template_name = 'update.html'
    fields = ('title', 'content')
    template_name_suffix = 'update'
    def get_success_url(self):
        return reverse('login:blog_complete', kwargs={'pk':self.object.pk})


class loggout_view(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login:logins'))