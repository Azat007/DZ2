from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Team


class AuthForm (AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        fields = ['username', 'password']
        # model = User


class RegistrationForm (UserCreationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
     
    class Meta:
        fields = ['username', 'password1', 'password2']
        model = User
        
        
class AddTeamForm(forms.Form):
    name = forms.CharField(required=True, 
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Имя', 'id': 'new_rec_name', 'maxlength': '49'}
        ),
        error_messages={'required': 'Please enter name'},
        label='Name'
    )
      
    country = forms.CharField(
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Город', 'id': 'new_rec_country', 'maxlength': '29'}
        )
    )
    
    sportType = forms.CharField(required=True,
        widget=forms.widgets.TextInput(
            attrs={'placeholder': 'Предмет', 'id': 'new_rec_sportType', 'maxlength': '29'}
        ),
        error_messages={'required': 'Please input name'},
        label='Предмет'
    )
    
    prizeCount = forms.IntegerField(required=True,
        widget=forms.widgets.NumberInput(
            attrs={
                'placeholder': 'Опыт',
                'id': 'new_rec_prizeCount', 
                'onKeyUp': 'if(this.value>999){this.value="999";}else if(this.value<0){this.value="0";}'
            }
        ),
        error_messages={'required': 'Please input'},
        label='Опыт'
    )    
    
    desc = forms.CharField(required=True,
        widget=forms.widgets.Textarea(
            attrs={'placeholder': 'Описание', 'id': 'new_rec_desc', 'maxlength': '1999'}
        ),
        error_messages={'required': 'Please input short description'},
        label='Предмет'
    )
    
    image = forms.FileField(required=False,
        widget=forms.widgets.ClearableFileInput(
            attrs={'accept':'image/jpeg, image/png, image/gif', 'id':'new_rec_img'}
        )
    )

    def fill_object(self):
        return Team.objects.create(
            name = self.cleaned_data['Имя'],
            country = self.cleaned_data['Город'],
            sportType = self.cleaned_data['Предмет'],
            prizeCount = int(self.cleaned_data['Опыт']),
            desc = self.cleaned_data['desc']
        )
    
    
    