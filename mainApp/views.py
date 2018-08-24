from django.shortcuts import render
from django.http import HttpResponse
from mainApp.models import Influencer, Events, Tags
from django.contrib.auth import login, authenticate

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
            Twitter.append(all_influencers[number].id)
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
