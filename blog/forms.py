from django import forms
from django.core.validators import ValidationError


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=10, label='your name')
    text = forms.CharField(max_length=10, label='your message')

    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        # if 'a' in name:
        #     self.add_error('name', 'a can not be in name')
        if name == text:
            raise ValidationError('name and text are not same', code='name_text_same')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # if 'a' in name:
        #     raise ValidationError('a can not be in name', code='a_in_name')
        # return name

        if name[0] == '0':                   #مثلا اینجا فیلد نام ، شماره تلفن همراه بگیره و میخوایم اگه کاراکتر اول صفر بود،صفر رو پاک کنه و ابتداش 98+ رو بذاره
            name = name.replace(name[0], "")
        return '+98' + name
