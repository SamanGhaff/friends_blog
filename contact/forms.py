from .models import Massage
from django import forms
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    year = ['2000', '2001', '2002']
    colors = [('blue', 'Blue'), ('green', 'Green')]
    text = forms.CharField(max_length=10, label="your massage")
    name = forms.CharField(max_length=10, label="your name")
    birth = forms.DateField(widget=forms.SelectDateWidget(years=year))
    color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=colors)

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise ValidationError('name and text are same', code="name_same_text")

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if "a" in name:
            raise ValidationError('no! a is not avaleble', code="name_a")
        return name


class MassageForm(forms.ModelForm):
    class Meta:
        model = Massage
        fields = ("title", "text", "email")
        widgets = {
            'title': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "enter your title:",
                "style": "background-color:#CAFF70",
            }),
            'text': forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "enter your massage:",
                "style": "background-color:#CAFF70",
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "enter your email:",
                "style": "background-color:#CAFF70",
            })
        }
