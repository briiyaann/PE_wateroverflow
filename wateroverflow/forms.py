from django import forms

class overFlowForm(forms.Form):
    row = forms.IntegerField(label="row")
    glass = forms.IntegerField(label="glass")
    water = forms.DecimalField(label="water")