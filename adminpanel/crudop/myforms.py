from django import forms

class UploadForm(forms.Form):
    name=forms.CharField()
    writer=forms.CharField()
    genre=forms.CharField()
    rate=forms.CharField()
    #forms.DecimalField(widget=forms.TextInput)
    review=forms.CharField()
    #forms.DecimalField(widget=forms.TextInput)
    upldate=forms.DateField()
    image=forms.FileField()

class UpdateForm(forms.Form):
    pid=forms.IntegerField(widget=forms.TextInput)
    name=forms.CharField()
    writer=forms.CharField()
    genre=forms.CharField()
    rate=forms.CharField()
    #forms.DecimalField(widget=forms.TextInput)
    review=forms.CharField()
    #forms.DecimalField(widget=forms.TextInput)
    upldate=forms.DateField()
