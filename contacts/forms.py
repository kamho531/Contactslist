from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):
    first_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}))
    last_name = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}))
    email = forms.EmailField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}))
    phone = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}))
    comment = forms.CharField(required=True, label="", widget=forms.widgets.TextInput(attrs={"placeholder":"Comment", "class":"form-control"}))

    class Meta:
        model = Contact
        exclude = ("user",)





