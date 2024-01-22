
from django import forms

from subscribe.models import Subscribe

from django.utils.translation import gettext_lazy as _

# from subscribe.models import Subscribe


class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields = '__all__'
        # exclude = ('first_name',)
        labels = {
            'first_name': _('Enter your first name'),
            'last_name' : _('Enter your last name'),
            'email': _('Enter your email')
        }
            
                   

        error_messages = {
            'first_name':{
                'required': _('You cannot move forward without first name')
            }
        }
# class SubscribeForm(forms.ModelForm):
#     class Meta:
#         model=Subscribe
#         fields = '__all__'

# def validate_comma(value):
#     if ',' in value:
#         raise forms.ValidationError('Invalid syntax')
#     return value
        

    # first_name = forms.CharField(max_length=100, required = False,label = 'Enter first name',help_text='Character only')
    # last_name = forms.CharField(max_length=100, disabled=False)
    # email = forms.EmailField(max_length=100)

