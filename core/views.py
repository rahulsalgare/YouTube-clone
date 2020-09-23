from django.shortcuts import render
from django.views import View
from .models import *
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.generic.edit import FormView, FormMixin
# from django.template import RequestContext, Template
from django.contrib.auth.models import User
import datetime
# Create your views here.
from haystack.forms import SearchForm
from haystack.generic_views import SearchView

class HomeView(SearchView):

    template_name = 'core/home.html'
    form_class = SearchForm

    def get_context_data(self, **kwargs):
        context = {}
        context['videos'] = Video.objects.all()
        context.update(kwargs)
        return super().get_context_data(**context)

class VideoView(DetailView, FormView):
    template_name = 'core/video.html'
    form_class = React

    def get_object(self, **kwargs):
        return Video.objects.get(id=self.kwargs['id'])

    # def get_form_class(self):
    #     return self.form_class

    def get_context_data(self, **kwargs):
        context = {}
        if self.object:
            context['object'] = self.object
            context['likes'] = self.object.userprofile_set.count()          #likes count by ManyToManyField reverse reference
            context['comments']=self.object.comment_set.all()   #comments by ForeignKey reverse reference

            if self.request.user.is_authenticated:
                if self.object.userprofile_set.filter(id=self.request.user.userprofile.id).exists():
                    context['likestatus'] = True
                else:
                    context['likestatus'] = False

        context.update(kwargs)
        return super().get_context_data(**context)

    def get_success_url(self):
        return reverse('core:videoview',kwargs={'id':self.kwargs['id']})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            print(form.cleaned_data['comment'])
            c_text = form.cleaned_data['comment']
            c_date = datetime.datetime.now()
            c_owner = request.user.userprofile
            c_video = Video.objects.get(id=self.kwargs['id'])

            newComment = Comment(comment_text=c_text,comment_datetime=c_date,
                                 comment_owner=c_owner,commented_video=c_video)
            newComment.save()
            return self.form_valid(form)

def register(request):
    template_name = 'registration/register.html'
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+username)
            us = UserProfile.objects.create(user = User.objects.get(username=username))
            us.save()
            return HttpResponseRedirect(reverse('core:login'))
    return render(request, template_name,{'form':form})

def profile(request,nm):
    template_name = 'core/profile.html'
    videos = Video.objects.filter(video_owner = request.user.userprofile.channel)
    print(videos)
    for v in videos:
        print(v)
    return render(request, template_name,{'videos':videos})

class VideoUploadView(FormView):
    template_name = 'core/videoupload.html'
    form_class = VideoForm
    # success_url = '/profile/'+ self.request.username

    def form_valid(self, form):
        form.save()

def likevideo(request):
    if request.method == 'GET':
        video_id = request.GET['video_id']
        vid = Video.objects.get(id=video_id)
        request.user.userprofile.liked_videos.add(vid)
        data = {
            'likescount': vid.userprofile_set.count()
        }
        return JsonResponse(data)

    else:
        return HttpResponse('Not Get')

def unlikevideo(request):
    if request.method == 'GET':
        video_id = request.GET['video_id']
        vid = Video.objects.get(id=video_id)
        request.user.userprofile.liked_videos.remove(vid)
        data = {
            'likescount':vid.userprofile_set.count()
        }
        return JsonResponse(data)
    else:
        return HttpResponse("no get")
