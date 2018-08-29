from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from mainApp.models import Influencer, Events, Tags
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.admin.widgets import FilteredSelectMultiple
from django import forms
from dal import autocomplete

def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
        userid = request.user.id
        all_influencers = Influencer.objects.filter(user = userid)

    Name =[]
    Email =[]
    Twitch =[]
    Twitter =[]
    Country =[]
    Shirt =[]
    Edit =[]
    Last_Updated =[]
    Mailing_Address =[]
    Phone =[]
    Youtube =[]
    tags =[]
    events =[]
    influencer = []

    try:
        for number in range(len(all_influencers)):
            Name.append(all_influencers[number].influencer_name)
            Email.append(all_influencers[number].email)
            Twitch.append(all_influencers[number].twitch)
            Twitter.append(all_influencers[number].twitter)
            Country.append(all_influencers[number].country)
            Shirt.append(all_influencers[number].shirt)
            influencer.append(all_influencers[number])
            timestamp = all_influencers[number].updated_at
            timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            Last_Updated.append(timestamp)
            Mailing_Address.append(all_influencers[number].mailing_address)
            Phone.append(all_influencers[number].phone)
            Youtube.append(all_influencers[number].youtube)
            hold = ""
            i_tags = all_influencers[number].tags.all()
            for item in i_tags:
                hold += item.tag_name + ', '
            hold = hold[:-2]
            tags.append(hold)
            hold = ""
            e_tags = all_influencers[number].events.all()
            for item in e_tags:
                hold += item.event_name + ', '
            hold = hold[:-2]
            events.append(hold)
    except:
        Name.append('Error')
        Email.append('Error')
        Twitch.append('Error')
        Twitter.append('Error')
        Country.append('Error')
        Shirt.append('Error')
        Last_Updated.append('Error')
        Mailing_Address.append('Error')
        Phone.append('Error')
        Youtube.append('Error')
        tags.append('Error')
        events.append('Error')
        influencer = 'Error'

    zipped = zip(
        Name,
        Email,
        Twitch,
        Twitter,
        Country,
        Shirt,
        influencer,
        Last_Updated,
        Mailing_Address,
        Phone,
        Youtube,
        tags,
        events,
        )

    return render(
        request,
        './index.html',
        context={'info':zipped}
    )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

class InfluencerCreateForm(forms.ModelForm):

    class Meta:
        model = Influencer
        fields = [
        'influencer_name',
        'email',
        'phone',
        'twitter',
        'youtube',
        'twitch',
        'shirt',
        'created_at',
        'updated_at',
        'country',
        'mailing_address',
        'notes',
        'tags',
        'events',
        ]
        widgets = {
            # 'tags': FilteredSelectMultiple("Tags",is_stacked=False,choices=Tags.objects.all()),
            'tags': forms.CheckboxSelectMultiple(),
            'events': forms.CheckboxSelectMultiple(),
        }

class InfluencerCreate(CreateView):
    temp_search = forms.TextInput()
    model = Influencer
    form_class = InfluencerCreateForm
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        influencer = form.save(commit=False)
        influencer.user = self.request.user
        influencer.save()
        return redirect('index')


class InfluencerUpdate(UpdateView):
    model = Influencer
    form_class = InfluencerCreateForm


class InfluencerDelete(DeleteView):
    template_name = 'delete.html'
    model = Influencer
    success_url = reverse_lazy('index')

class TagCreate(CreateView):
    model = Tags
    fields = [
    'tag_name'
    ]
    success_url = reverse_lazy('index')


class TagUpdate(UpdateView):
    model = Tags
    fields = [
    'tag_name'
    ]
    success_url = reverse_lazy('index')

class TagDelete(DeleteView):
    template_name = 'delete.html'
    model = Tags
    success_url = reverse_lazy('index')

class EventCreate(CreateView):
    model = Events
    fields = [
    'event_name'
    ]
    success_url = reverse_lazy('index')


class EventUpdate(UpdateView):
    model = Events
    fields = [
    'event_name'
    ]
    success_url = reverse_lazy('index')

class EventDelete(DeleteView):
    template_name = 'delete.html'
    model = Events
    success_url = reverse_lazy('index')
#
# class TagAutoComplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         qs = Tags.objects.all()
#
#         if self.q:
#             qs = qs.filter(tag_name__istartswith=self.q)
#         return qs
