from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from mainApp.models import Influencer, Events, Tags, List
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import InfluencerCreateForm, TagFormCSV, EventFormCSV, TagForm, EventForm, ListCreateForm, InfluencerCSVForm
from django import forms
from django.utils.html import strip_tags
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import csv

def Test(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response


def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
        userid = request.user.id
        all_influencers = Influencer.objects.filter(user = userid)

    Handle=[]
    Name=[]
    Email=[]
    Twitch=[]
    Twitter=[]
    Youtube=[]
    Mixer=[]
    Country=[]
    Shirt=[]
    Edit=[]
    Last_Updated=[]
    Mailing_Address=[]
    Phone=[]
    tags=[]
    events=[]
    influencer=[]
    lists=[]

    try:
        for number in range(len(all_influencers)):
            Handle.append(all_influencers[number].influencer_handle)
            Name.append(all_influencers[number].legal_name)
            Email.append(all_influencers[number].email)
            Phone.append(all_influencers[number].phone)
            Twitch.append(all_influencers[number].twitch)
            Twitter.append(all_influencers[number].twitter)
            Youtube.append(all_influencers[number].youtube)
            Mixer.append(all_influencers[number].mixer)
            Country.append(all_influencers[number].country)
            Shirt.append(all_influencers[number].shirt)
            influencer.append(all_influencers[number])
            timestamp = all_influencers[number].updated_at
            timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
            Last_Updated.append(timestamp)
            Mailing_Address.append(all_influencers[number].mailing_address)
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
            query = List.objects.filter(list_influencers__influencer_handle = all_influencers[number].influencer_handle)
            print('q',query)
            for item in query:
                hold += item.list_name + ', '
            print('h',hold)
            hold = hold[:-2]
            lists.append(hold)
    except:
        Handle.append('Error')
        Name.append('Error')
        Email.append('Error')
        Twitch.append('Error')
        Twitter.append('Error')
        Youtube.append('Error')
        Mixer.append('Error')
        Country.append('Error')
        Shirt.append('Error')
        Last_Updated.append('Error')
        Mailing_Address.append('Error')
        Phone.append('Error')
        tags.append('Error')
        events.append('Error')
        influencer = 'Error'
        lists.append('Error')

    zipped = zip(
        Handle,
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
        Mixer,
        tags,
        events,
        lists,
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

@login_required
def InfluencerCreate(request):
    if request.method == 'POST':
        form = InfluencerCreateForm( request.user, request.POST, )
        if form.is_valid():
            influencer = form.save(commit=False)
            influencer.user = request.user
            influencer.save()
            return redirect('index')
    else:
        form = InfluencerCreateForm(request.user)
    return render(request, 'mainApp/influencer_form.html', {'form': form})

def InfluencerCreateCSV(request):
    if request.method == 'POST':
        form = InfluencerCSVForm(request.POST)
        if form.is_valid():
            username = request.user
            # userid = request.user.id
            fields = form['seperate_fields_with_commas'].value()
            print('fields', fields)
            stripped_fields = strip_tags(fields).strip()
            print('stripped_fields',stripped_fields)
            field_array = stripped_fields.split(",")
            field_array = list(map(str.strip, field_array))
            print('field_array',field_array)
            data = form['paste_CSV']
            stripped_data = strip_tags(data).strip()
            data_array = stripped_data.split(",")
            print('data_array',data_array)
            passed = []
            failed = []
            test_against = ['influencer_handle','legal_name','email','phone','twitter','youtube','twitch','mixer','shirt','country']
            for element in field_array:
                if element in test_against:
                    passed.append(element)
                    print(element, "Is a field catagory!!!!!!!!!")
                else:
                    print(element, "Is not a field catagory")
            for element in test_against:
                if element not in field_array:
                    failed.append(element)
                    print(element, "Field is not being populated")
            print('passed', passed)
            print('failed', failed)
            Handle=[]
            Name=[]
            Email=[]
            Twitch=[]
            Twitter=[]
            Youtube=[]
            Mixer=[]
            Country=[]
            Shirt=[]
            Phone=[]
            pointer = 0
            for item in data_array:
                print('passed item', item)
                catagory = passed[pointer]
                if catagory == 'influencer_handle':
                    Handle.append(item)
                elif catagory == 'legal_name':
                    Name.append(item)
                elif catagory == 'email':
                    Email.append(item)
                elif catagory == 'phone':
                    Phone.append(item)
                elif catagory == 'twitter':
                    Twitter.append(item)
                elif catagory == 'youtube':
                    Youtube.append(item)
                elif catagory == 'twitch':
                    Twitch.append(item)
                elif catagory == 'mixer':
                    Mixer.append(item)
                elif catagory == 'shirt':
                    Shirt.append(item)
                elif catagory == 'country':
                    Country.append(item)
                pointer += 1
                print('p',pointer)
                if pointer >= len(passed):
                    pointer -= len(passed)
            for item in range(len(Handle)):
                print('Failed item', item)
                if 'influencer_handle' in failed:
                    Handle.append("")
                if 'legal_name' in failed:
                    Name.append("")
                if 'email' in failed:
                    Email.append("")
                if 'phone' in failed:
                    Phone.append("")
                if 'twitter' in failed:
                    Twitter.append("")
                if 'youtube' in failed:
                    Youtube.append("")
                if 'twitch' in failed:
                    Twitch.append("")
                if 'mixer' in failed:
                    Mixer.append("")
                if 'shirt' in failed:
                    Shirt.append("")
                if 'country' in failed:
                    Country.append("")
            print('Handle',Handle, len(Handle))
            print('Email',Email, len(Email))
            for item in range(len(Handle)):
                print('item no #', item)
                try:
                    new_influencer = Influencer(user=username, influencer_handle=Handle[item], legal_name=Name[item], email=Email[item], phone=Phone[item], twitter=Twitter[item], youtube=Youtube[item],twitch=Twitch[item],mixer=Mixer[item],shirt=Shirt[item],country=Country[item])
                    new_influencer.save()
                except Exception as inst:
                    print("Failed to create influencer: ",Handle[item])
                    print(type(inst))
                    print(inst.args)
                    print(inst)
            return redirect('index')
    form = InfluencerCSVForm()
    return render(request, 'mainApp/influencer_csv_form.html', {'form':form})




@login_required
def InfluencerUpdate(request, pk):
    object = Influencer.objects.get(id = pk)
    if request.method == 'POST':
        form = InfluencerCreateForm( request.user, request.POST, instance = object, )
        if form.is_valid():
            influencer = form.save(commit=True)
            return redirect('index')
    else:
        form = InfluencerCreateForm(request.user, instance = object, )
    edit = form['influencer_handle'].value()
    print('e',edit)
    context = {
        'form':form,
        'edit':edit,
        'pk':pk
    }
    return render(request, 'mainApp/influencer_form.html', context)

#@login_required
class InfluencerDelete(DeleteView):
    template_name = 'delete.html'
    model = Influencer
    success_url = reverse_lazy('index')

#@login_required
class TagCreate(CreateView):
    model = Tags
    fields = [
    'tag_name'
    ]
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        tagForm = form.save(commit=False)
        tagForm.tag_name = tagForm.tag_name.upper()
        check = tagForm.tag_name
        obj, created = Tags.objects.get_or_create(tag_name = check, tag_user = self.request.user)
        if not created:
            print(obj.get_absolute_url())
            return redirect(obj.get_absolute_url())
        else:
            return redirect('index')

@login_required
def TagCreateCSV(request):
    form = TagFormCSV()
    if request.method == 'POST':
        form = TagFormCSV(request.POST)
        if form.is_valid():
            data = form['seperate_tags_with_commas']
            stripped_data = strip_tags(data).strip()
            tag_array = stripped_data.split(",")
            created_tags = []
            for tag in tag_array:
                tag = tag.strip()
                tag = tag.upper()
                if tag == '':
                    continue
                query = Tags.objects.filter(tag_name=tag )
                query = query.filter(tag_user=request.user)
                exists = len(query)
                if not exists:
                    new_tag = Tags.objects.create(tag_name = tag, tag_user = request.user)
                    new_tag.save
                    created_tags.append(tag)
            return render(
                            request,
                            'mainApp/tag_csv_form.html',
                            {
                                'form':form,
                                'created':created_tags
                            }
                        )
    return render(request, 'mainApp/tag_csv_form.html', {'form':form})

@login_required
def TagUpdate(request, pk):
    tag = get_object_or_404(Tags, tag_user=request.user, id=pk)
    exists = False
    if request.POST:
        form = TagForm(request.POST, instance=tag)
        test = form['tag_name'].value()
        try:
            check = Tags.objects.get(tag_user=request.user, tag_name=test)
            exists = test
        except:
            pass
        if not exists:
            if form.is_valid():
                form.save()
                return redirect('index')
    test = tag.tag_name
    form = TagForm(instance=tag)
    print(form)
    context = { 'form':form,
                'id':pk,
                'test':test,
                'exists':exists}
    return render(request,'mainApp/tags_update.html',context)

#@login_required
class TagDelete(DeleteView):
    template_name = 'delete.html'
    model = Tags
    success_url = reverse_lazy('index')

#@login_required
class EventCreate(CreateView):
    model = Events
    fields = [
    'event_name'
    ]
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        eventForm = form.save(commit=False)
        check = eventForm.event_name.upper()
        obj, created = Events.objects.get_or_create(event_name = check, event_user = self.request.user)
        if not created:
            print(obj.get_absolute_url())
            return redirect(obj.get_absolute_url())
        else:
            return redirect('index')

@login_required
def EventCreateCSV(request):
    form = EventFormCSV()
    if request.method == 'POST':
        form = EventFormCSV(request.POST)
        if form.is_valid():
            data = form['seperate_events_with_commas']
            stripped_data = strip_tags(data).strip()
            event_array = stripped_data.split(",")
            created_events = []
            for event in event_array:
                event = event.strip()
                event = event.upper()
                if event == '':
                    continue
                query = Events.objects.filter(event_name=event )
                query = query.filter(event_user=request.user)
                exists = len(query)
                if not exists:
                    new_event = Events.objects.create(event_name = event, event_user = request.user)
                    new_event.save
                    created_events.append(event)
            return render(
                            request,
                            'mainApp/event_csv_form.html',
                            {
                                'form':form,
                                'created':created_events
                            }
                        )
    return render(request, 'mainApp/event_csv_form.html', {'form':form})

@login_required
def EventUpdate(request, pk):
    event = get_object_or_404(Events, event_user=request.user, id=pk)
    exists = False
    if request.POST:
        form = EventForm(request.POST, instance=event)
        test = form['event_name'].value()
        try:
            check = Events.objects.get(event_user=request.user, event_name=test)
            exists = test
        except:
            pass
        if not exists:
            if form.is_valid():
                form.save()
                return redirect('index')
    test = event.event_name
    form = EventForm(instance=event)
    print(form)
    context = { 'form':form,
                'id':pk,
                'test':test,
                'exists':exists}
    return render(request,'mainApp/events_update.html',context)

#@login_required
class EventDelete(DeleteView):
    template_name = 'delete.html'
    model = Events
    success_url = reverse_lazy('index')

@login_required
def lists(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
        userid = request.user.id
        all_lists = List.objects.filter(list_user = userid)
    Name = []
    influencers = []
    Links = []
    try:
        for number in range(len(all_lists)):
            Name.append(all_lists[number].list_name)
            i_name = []
            i_link = []
            list_influencer = all_lists[number].list_influencers.all()
            for item in list_influencer:
                i_name.append(item.influencer_handle)
                i_link.append(item.get_absolute_url)
            i_data = zip(
                i_name,
                i_link
            )
            # hold = hold[:-2]
            influencers.append(i_data)
            Links.append(all_lists[number])
    except:
        Name.append('Error')
        influencers.append('Error')
        Links.append('Error')
    zipped = zip(
        Name,
        influencers,
        Links,
        )

    return render(request,'mainApp/list-home.html',context={'info':zipped})

@login_required
def ListCreate(request):
    if request.method == 'POST':
        form = ListCreateForm(request.user, request.POST)
        if form.is_valid():
            people = form.save(commit=False)
            name = people.list_name
            check = List.objects.filter(list_user = request.user, list_name = name)
            if not len(check):
                people.list_user = request.user
                people.save()
                form.save_m2m()
                return redirect('lists-home')
            else:
                context = {
                    'exists':name,
                    'form': form,
                }
                return render(request, 'mainApp/list_form.html', context)

    else:
        form = ListCreateForm(request.user)
    return render(request, 'mainApp/list_form.html', {'form': form})

@login_required
def ListUpdate(request, pk):
    list = get_object_or_404(List, list_user=request.user, list_id=pk)
    original = list.list_name
    update = True
    exists = False
    if request.POST:
        form = ListCreateForm(request.user,request.POST, instance=list)
        test = form['list_name'].value()
        if not original == test:
            try:
                check = List.objects.get(list_user=request.user, list_name=test)
                exists = test
            except:
                pass
        if not exists:
            if form.is_valid():
                form.save()
                return redirect('lists-home')
    test = list.list_name
    form = ListCreateForm(request.user, instance=list)
    print(form)
    context = { 'form':form,
                'id':pk,
                'test':test,
                'exists':exists,
                'update':update}
    return render(request,'mainApp/list_form.html',context)
#
# class ListUpdate(UpdateView):
#     model = List
#     fields = [
#     'list_name',
#     'list_influencers'
#     ]
#     success_url = reverse_lazy('lists-home')
#@login_required
class ListDelete(DeleteView):
    template_name = 'delete.html'
    model = List
    success_url = reverse_lazy('lists-home')
