
from django import forms

class FeedbackForm(forms.Form):
    Name = forms.CharField(
        max_length = 30,
        widget = forms.TextInput(
            attrs={'class'          : 'form-control',
                   'type'           : 'text',
                   'id'             : 'name',
                   'placeholder'    : 'Enter Your Name',
                   'name'           : 'name',
                   }
                               )
                           )
    Email = forms.CharField(
        max_length = 50,
        widget = forms.TextInput(
            attrs={'class'          : 'form-control',
                   'type'           : 'text',
                   'id'             : 'email',
                   'placeholder'    : 'Enter Your Email',
                   'name'           : 'email',
                   }
                               )
                           )
    Feedback = forms.CharField(
        max_length = 1000,
        widget = forms.TextInput(
            attrs={'class'          : 'form-control',
                   'id'             : 'message',
                   'placeholder'    : 'Enter Your Feedback',
                   'name'           : 'message',
                   'rows'           : '3',
                   }
                               )
                           )
