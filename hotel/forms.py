from django import forms
from hotel.models import hotels_data

class HotelForm(forms.ModelForm):
    hotel_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':50}))
    zipcode = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    about_hotel = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':110}))
    facebook = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    instagram = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    linkdin = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    twitter = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    google_user = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    website = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    latitude = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    longitude = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    dest_choices =(
    ("Goa", "Goa"), 
    ("Chennai", "Chennai"),
    ("Mumbai", "Mumbai"),
    ("Kolkata", "Kolkata"),
    ("Delhi", "Delhi"),
    ("Madhya Pradesh", "Madhya Pradesh")
    )
    destination = forms.ChoiceField(choices = dest_choices,widget=forms.Select(attrs={"class":"form-control",}))

    class Meta:
        model = hotels_data
        fields= "__all__"