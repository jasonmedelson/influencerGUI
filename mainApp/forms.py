from django import forms
from .models import Influencer, Tags, Events

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
