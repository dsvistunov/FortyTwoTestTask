from django.forms import ModelForm, FileInput, Textarea
from .models import Profile


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = [
            'first_name', 'last_name', 'date_birth', 'email',
            'jabber', 'skype', 'other_contacts', 'bio', 'photo'
        ]
        widgets = {
            'photo': FileInput(attrs={
                'placeholder': 'user_photo'
            }),
            'other_contacts': Textarea(attrs={
                'cols': 40,
                'rows': 9,
                'placeholder': 'other_contacts'
            }),
            'bio': Textarea(attrs={
                'cols': 40,
                'rows': 9,
                'placeholder': 'bio'
            })
        }
