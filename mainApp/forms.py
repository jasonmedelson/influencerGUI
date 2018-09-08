from django import forms
from .models import Influencer, Tags, Events, List

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
    def __init__(self, user, *args, **kwargs):
        # self.user = kwargs.pop('user', None)
        # del kwargs['user']

        super(InfluencerCreateForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tags.objects.filter(tag_user=user)
        self.fields['events'].queryset = Events.objects.filter(event_user=user)



class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = [
            'list_name',
            'influencers',
        ]
        widgets = {
            'influencers': forms.CheckboxSelectMultiple(),
        }
    def __init__(self, user, *args, **kwargs):
        super(ListForm,self).__init__(*args,**kwargs)
        self.fields['influencers'].queryset = Influencer.objects.filter(user=user)


class TagFormCSV(forms.Form):
    seperate_tags_with_commas = forms.CharField(widget=forms.Textarea)

class EventFormCSV(forms.Form):
    seperate_events_with_commas = forms.CharField(widget=forms.Textarea)

class TagForm(forms.ModelForm):
    class Meta:
        model = Tags
        fields = [
        'tag_name'
        ]

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = [
        'event_name'
        ]
