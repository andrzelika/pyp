from django import forms
from blog.models import CzlonekRodziny

class CzlonekRodzinyForm(forms.ModelForm):
    class Meta:
        model = CzlonekRodziny
        fields = ['imie', 'nazwisko', 'wiek']

class HelloForm(forms.Form):
    name = forms.CharField(label=u'Your name', max_length=20)
