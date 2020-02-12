from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import Snippet


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Name*'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email*'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Phone*'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message*'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('name', 'email', 'phone', 'message', css_class='form-group')
            ),
            Column(Submit('Submit', 'Send Message', css_class='btn btn-primary btn-xl')),
        )

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'email', 'phone', 'message')

