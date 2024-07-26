from django import forms
class dateinput(forms.DateInput):
    input_type='date'
class Contact(forms.Form):
    name=forms.CharField(max_length=225)
    email=forms.EmailField() 
    date=forms.DateField(widget=dateinput)
class Date(forms.Form):
    class meta:
        widgets={'date':dateinput()}  