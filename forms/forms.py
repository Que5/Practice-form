from django import forms
from .models import Form
# from phonenumber_field.widgets import PhoneNumberPrefixWidget

class ContactForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
        # widgets = {
        #     'mobile_number': PhoneNumberPrefixWidget(),
        # }