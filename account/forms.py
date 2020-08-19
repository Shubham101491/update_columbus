from django import forms
from django.contrib.auth.models import User
from .models import user_register
from category.models import user_type, User_category

# Sign Up Form
class register(forms.ModelForm):
    phone = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'forms_field-input', 'placeholder': "Phone number", 'name': 'phone'}))

    # join_as = forms.ModelChoiceField(required=True, empty_label="Please select type", queryset=user_type.objects.filter(
    #     publish_status=True), widget=forms.Select(attrs={"class": "forms_field-input", 'multiple': 'multiple', 'name': 'join_as'}))

    category = forms.ModelChoiceField(required=True, empty_label="Please select category", queryset=User_category.objects.filter(
        publish_status=True), widget=forms.Select(attrs={"class": "forms_field-input", 'name': 'category'}))

    discount_min = forms.IntegerField(widget=forms.NumberInput(
        attrs={"class": "forms_field-input wd-36", "min": "1", "max": "50", 'placeholder': "5%", 'name': 'discount_min'}))
    discount_max = forms.IntegerField(widget=forms.NumberInput(
        attrs={"class": "forms_field-input wd-36", "min": "1", "max": "50", 'placeholder': "50%", 'name': 'discount_max'}))

    class Meta:
        model = user_register
        fields = ['phone', 'join_as', 'category',
                  'discount_min', 'discount_max']