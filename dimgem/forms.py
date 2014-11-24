from django import forms


class SearchingForm(forms.Form):
    word = forms.CharField(label='Wpisz szukaną frazę')
