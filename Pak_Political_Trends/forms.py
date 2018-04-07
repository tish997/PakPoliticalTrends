from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Pak_Political_Trends.models import TrendsForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'E-Mail', 'required': True}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Username', 'required': True}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'First Name', 'required': True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Last Name', 'required': True}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Password', 'required': True}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Confirm Password', 'required': True}))

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class TrendsInputForm(forms.Form):
    topic = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Topic/Politician Name'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Date To e.g. 10/25/06',
                                                            'required': True}))
    from_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Date Form e.g. 10/25/06',
                                                              'required': True}))

    class Meta:
        model = TrendsForm
        fields = (
            'topic',
            'to_date',
            'from_date',
        )

