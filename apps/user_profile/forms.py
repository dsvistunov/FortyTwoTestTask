from django.forms import ModelForm
from .models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name', 'date_birth', 'email',
            'jabber', 'skype', 'other_contacts', 'bio'
        ]
