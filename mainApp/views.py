from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainApp.models import Influencer, Events, Tags
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    username = None
    if request.user.is_authenticated:
        username = request.user
        userid = request.user.id
        all_influencers = Influencer.objects.filter(user = userid)
    Name = []
    Email = []
    Phone = []
    Country = []
    Shirt = []
    Twitter = []
    try:
        for number in range(len(all_influencers)):
            Name.append(all_influencers[number].influencer_name)
            Email.append(all_influencers[number].email)
            Phone.append(all_influencers[number].phone)
            Country.append(all_influencers[number].country)
            Shirt.append(all_influencers[number].shirt)
            Twitter.append(all_influencers[number].tags.all())
    except:
        Name.append('Error')
        Email.append('Error')
        Phone.append('Error')
        Country.append('Error')
        Shirt.append('Error')
        Twitter.append('Error')

    zipped = zip(Name,
        Email,
        Phone,
        Country,
        Shirt,
        Twitter,
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
